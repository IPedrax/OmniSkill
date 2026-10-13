#!/usr/bin/env python3
"""Content-aware image resize (seam carving): change an image's size or aspect ratio by
removing or adding the least interesting pixel paths, so subjects keep their shape.

    smartresize.py in.jpg out.jpg --width 800                  # shrink to 800 wide
    smartresize.py in.jpg out.jpg --aspect 9:16                # reframe, carving the long side
    smartresize.py in.jpg out.jpg --width 1400 --keep 300,120,400,500
    smartresize.py in.jpg out.jpg --perc 30                    # remove 30% of the width
    smartresize.py selftest

--keep x,y,w,h protects a box (a face, a product, text); --drop x,y,w,h makes a box the first
thing to go. Both repeat. Needs numpy and Pillow.
"""
import argparse
import sys

import numpy as np
from PIL import Image

BIG = 1e6  # energy for protected (+) and doomed (-) pixels


def energy(rgb):
    g = rgb[..., :3].astype(np.float32) @ np.array([0.299, 0.587, 0.114], np.float32)
    gy, gx = np.gradient(g)
    return np.abs(gx) + np.abs(gy)


def find_seam(e):
    """Cheapest top-to-bottom 8-connected path: column index per row."""
    h, w = e.shape
    cost = np.full((h, w + 2), np.inf, np.float32)  # inf border keeps seams inside the image
    cost[:, 1:-1] = e
    back = np.zeros((h, w), np.int8)
    for y in range(1, h):
        l, c, r = cost[y - 1, :-2], cost[y - 1, 1:-1], cost[y - 1, 2:]
        left, right = l < c, r < np.minimum(l, c)
        back[y] = np.where(right, 1, np.where(left, -1, 0))
        cost[y, 1:-1] += np.where(right, r, np.where(left, l, c))
    seam = np.empty(h, np.int64)
    seam[-1] = int(np.argmin(cost[-1, 1:-1]))
    for y in range(h - 1, 0, -1):
        seam[y - 1] = seam[y] + back[y, seam[y]]
    return seam


def drop_col(a, seam):
    h, w = a.shape[:2]
    j = np.arange(w - 1)[None, :] + (np.arange(w - 1)[None, :] >= seam[:, None])
    flat = (np.arange(h)[:, None] * w + j).ravel()
    return a.reshape((h * w,) + a.shape[2:])[flat].reshape((h, w - 1) + a.shape[2:])


def carve(img, n, bias):
    """Remove n vertical seams. bias: float32 array added to energy (>0 keep, <0 drop).
    Returns the image and, per seam, the original column of each row (for enlarging)."""
    h, w = img.shape[:2]
    cols = np.tile(np.arange(w), (h, 1))
    seams = []
    for _ in range(n):
        s = find_seam(energy(img) + bias)
        seams.append(cols[np.arange(h), s].copy())
        img, bias, cols = drop_col(img, s), drop_col(bias, s), drop_col(cols, s)
    return img, seams


def enlarge(img, n, bias):
    """Add n vertical seams: carve a copy to find them, then duplicate those paths."""
    _, seams = carve(img.copy(), n, bias.copy())
    h, w = img.shape[:2]
    out = []
    for y in range(h):
        row = img[y].astype(np.float32)
        cs = np.array(sorted(s[y] for s in seams))
        nxt = row[np.minimum(cs + 1, w - 1)]
        out.append(np.insert(row, cs + 1, (row[cs] + nxt) / 2, axis=0))
    return np.stack(out).round().clip(0, 255).astype(np.uint8)


def resize_axis(img, target, bias):
    """Make width equal to target by carving or inserting seams."""
    w = img.shape[1]
    if target < w:
        return carve(img, w - target, bias)[0], None
    if target > w:
        return enlarge(img, target - w, bias), None
    return img, None


def smart_resize(img, width=None, height=None, keep=(), drop=()):
    """img: HxWxC uint8. Returns the resized array. ponytail: python loop per seam row, so
    a 4000 px photo is slow; shrink with a plain resize first when the change is under 20%."""
    h, w = img.shape[:2]
    bias = np.zeros((h, w), np.float32)
    for x, y, bw, bh in keep:
        bias[y:y + bh, x:x + bw] = BIG
    for x, y, bw, bh in drop:
        bias[y:y + bh, x:x + bw] = -BIG
    if width and width != w:
        img, _ = resize_axis(img, width, bias)
        bias = _after(bias, w, width)
    if height and height != h:
        t = np.ascontiguousarray(img.swapaxes(0, 1))
        t, _ = resize_axis(t, height, np.ascontiguousarray(bias.T))
        img = np.ascontiguousarray(t.swapaxes(0, 1))
    return img


def _after(bias, old_w, new_w):
    """Protection is a hint for the first axis only; drop it for the second."""
    return np.zeros((bias.shape[0], new_w), np.float32)


def aspect_size(w, h, ratio):
    a, b = (float(x) for x in ratio.split(":"))
    target = a / b
    return (round(h * target), None) if w / h > target else (None, round(w / target))


def box(s):
    x, y, w, h = (int(v) for v in s.split(","))
    return x, y, w, h


def selftest():
    h, w = 120, 200
    img = np.zeros((h, w, 3), np.uint8)
    img[..., 0] = np.linspace(40, 90, w, dtype=np.uint8)
    img[40:80, 80:120] = (255, 0, 0)  # subject: 40x40 red square, plus a busy stripe
    img[:, 10:18] = np.random.default_rng(1).integers(0, 255, (h, 8, 3), np.uint8)
    red = lambda a: int(((a[..., 0] > 250) & (a[..., 1] < 5)).sum())
    out = smart_resize(img, width=140)
    assert out.shape == (h, 140, 3) and red(out) == 1600, (out.shape, red(out))
    out = smart_resize(img, width=260)
    assert out.shape == (h, 260, 3) and red(out) >= 1600
    out = smart_resize(img, height=90)
    assert out.shape == (90, w, 3)
    out = smart_resize(img, width=140, keep=[(80, 40, 40, 40)])
    assert red(out) == 1600
    assert aspect_size(200, 120, "9:16")[0] == 68 and aspect_size(100, 400, "16:9")[1] == 56
    print("selftest ok")


def main():
    if sys.argv[1:] == ["selftest"]:
        return selftest()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--width", type=int)
    ap.add_argument("--height", type=int)
    ap.add_argument("--perc", type=float, help="remove this %% of the width (negative adds)")
    ap.add_argument("--aspect", help="W:H, e.g. 9:16; carves the side that is too long")
    ap.add_argument("--keep", type=box, action="append", default=[], help="x,y,w,h to protect")
    ap.add_argument("--drop", type=box, action="append", default=[], help="x,y,w,h to remove first")
    a = ap.parse_args()
    im = Image.open(a.src)
    mode = "RGBA" if "A" in im.getbands() else "RGB"
    arr = np.asarray(im.convert(mode))
    h, w = arr.shape[:2]
    width, height = a.width, a.height
    if a.perc:
        width = round(w * (1 - a.perc / 100))
    if a.aspect:
        width, height = aspect_size(w, h, a.aspect)
    if not (width or height):
        sys.exit("give --width, --height, --perc or --aspect")
    out = smart_resize(arr, width, height, a.keep, a.drop)
    Image.fromarray(out, mode).save(a.dst)
    print(f"{w}x{h} -> {out.shape[1]}x{out.shape[0]}  {a.dst}")


if __name__ == "__main__":
    main()
