# Framer Motion (motion) — Pattern Cookbook

Import from `motion/react` (current package). Legacy projects use `framer-motion`.
All examples are React + TypeScript; strip types for `.jsx`.

```tsx
import { motion, AnimatePresence, useScroll, useTransform, useInView } from "motion/react";
```

> **Next.js / Remix / Astro:** `motion` components are client-side. Add `"use client"` at the
> top of any file using them in the Next.js App Router, or render inside a React island in Astro.

---

## 1. Entrance / reveal

```tsx
<motion.div
  initial={{ opacity: 0, y: 24 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }} // easeOutExpo-ish
>
  Content
</motion.div>
```

## 2. Scroll-triggered (in-view, once)

```tsx
const ref = useRef(null);
const inView = useInView(ref, { once: true, margin: "-80px" });
return (
  <motion.section
    ref={ref}
    initial={{ opacity: 0, y: 40 }}
    animate={inView ? { opacity: 1, y: 0 } : {}}
    transition={{ duration: 0.6 }}
  />
);
```

## 3. Staggered list / grid

```tsx
const container = { hidden: {}, show: { transition: { staggerChildren: 0.08 } } };
const item = { hidden: { opacity: 0, y: 16 }, show: { opacity: 1, y: 0 } };

<motion.ul variants={container} initial="hidden" whileInView="show" viewport={{ once: true }}>
  {items.map((x) => <motion.li key={x.id} variants={item}>{x.label}</motion.li>)}
</motion.ul>
```

## 4. Hover / tap micro-interactions (buttons, cards)

```tsx
<motion.button
  whileHover={{ scale: 1.03, y: -2 }}
  whileTap={{ scale: 0.97 }}
  transition={{ type: "spring", stiffness: 400, damping: 25 }}
>
  Click me
</motion.button>
```

## 5. Mount / unmount (modals, toasts)

```tsx
<AnimatePresence>
  {open && (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      transition={{ duration: 0.2 }}
    />
  )}
</AnimatePresence>
```

## 6. Shared layout / magic-move

```tsx
<motion.div layout transition={{ type: "spring", stiffness: 300, damping: 30 }} />
// Same layoutId across two elements animates between their positions:
<motion.div layoutId="card-1" />
```

## 7. Scroll-linked parallax / progress

```tsx
const { scrollYProgress } = useScroll();
const y = useTransform(scrollYProgress, [0, 1], ["0%", "30%"]);
<motion.div style={{ y }} />
// Progress bar:
<motion.div style={{ scaleX: scrollYProgress, transformOrigin: "0%" }} className="h-1 bg-indigo-500" />
```

## 8. Page transitions (Next App Router)

```tsx
"use client";
import { motion } from "motion/react";
export default function Template({ children }: { children: React.ReactNode }) {
  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.3 }}>
      {children}
    </motion.div>
  );
}
```

---

## Tasteful defaults (use these unless the design calls for otherwise)

| Intent              | Values                                                            |
| ------------------- | ---------------------------------------------------------------- |
| Standard ease       | `transition={{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }}`       |
| Springy / playful   | `transition={{ type: "spring", stiffness: 400, damping: 25 }}`   |
| Subtle entrance     | `y: 16–24`, `opacity 0→1`, `duration 0.4–0.6`                    |
| Stagger             | `staggerChildren: 0.06–0.1`                                       |
| Hover lift          | `scale: 1.02–1.04`, `y: -2`                                       |

## Accessibility — always honor reduced motion

```tsx
import { useReducedMotion } from "motion/react";
const reduce = useReducedMotion();
const variants = reduce
  ? { hidden: { opacity: 0 }, show: { opacity: 1 } }          // fade only
  : { hidden: { opacity: 0, y: 24 }, show: { opacity: 1, y: 0 } };
```

Or globally wrap the app in `<MotionConfig reducedMotion="user">`.

## Performance rules
- Animate only `transform` (x/y/scale/rotate) and `opacity` — they're GPU-composited.
- Avoid animating `width`/`height`/`top`/`left`; use `layout` or `scale` instead.
- Add `will-change` sparingly; motion handles it for animated props.
- For long lists, prefer `whileInView` with `viewport={{ once: true }}` over always-on animation.
