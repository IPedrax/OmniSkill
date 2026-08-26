# Motion Craft — timing, easing, choreography

The other cookbooks answer *which library* and *what to type*. This one answers the question that
actually decides whether the result looks professional: **how should it move.**

Engine-agnostic. Every number here maps onto Framer Motion, GSAP, anime.js, CSS, or a spring.

---

## The one rule

**Motion explains a change of state.** Something appeared, something left, something moved, something
is loading, something responded to you. If nothing changed, nothing should move.

Most bad UI animation fails this before any of the numbers matter: elements that were always there
fading in on scroll, a CTA pulsing forever, a page that animates on every route change including
back. Delete those. The remaining ones are worth tuning.

---

## Duration

Scale duration to **distance and area**, never to importance. An important button does not get a
slower hover; it gets a better one.

| What is moving | Band |
| --- | --- |
| Micro feedback: hover, tap, toggle, focus ring, checkbox | **100–150 ms** |
| Small element: tooltip, dropdown, icon morph, inline expand | **150–250 ms** |
| Standard component: modal, drawer, toast, card, accordion | **250–400 ms** |
| Large surface: full-screen overlay, page or route transition | **400–600 ms** |
| Scroll-scrubbed | no duration; it is bound to progress |
| Ambient / looping background | **3 s+**, low amplitude, never near the content |

Doubling the travel distance does not double the time. Go up about half a band.

**Exits run at roughly two thirds of the entrance.** The user has already decided; do not make them
wait for the thing they just dismissed. A 300 ms modal open pairs with a 200 ms close.

Anything over 600 ms that is not scroll-bound or deliberately editorial is a bug, not a style.

---

## Easing

Easing is chosen by **what the element is doing**, not by taste:

| Situation | Ease | Concretely |
| --- | --- | --- |
| Entering and coming to rest | **ease-out** | `cubic-bezier(0.22, 1, 0.36, 1)` · `power3.out` · `outExpo` |
| Leaving the screen | **ease-in** | `cubic-bezier(0.4, 0, 1, 1)` · `power2.in` · `inQuad` |
| Moving between two on-screen positions | **ease-in-out** | `cubic-bezier(0.65, 0, 0.35, 1)` · `power2.inOut` |
| Scroll-scrubbed | **linear, always** | `ease: "none"` |
| Follows the user's finger or pointer | **spring** | see below |

Two easings to avoid: the CSS default `ease` (mushy on everything), and `linear` on a timed
animation (reads mechanical, because nothing physical starts at full speed).

An eased tween on a scrubbed ScrollTrigger double-eases against the scroll position and feels like
input lag. That is the single most common scroll-animation mistake.

### Springs

| Feel | Values | Use for |
| --- | --- | --- |
| Snappy UI | `stiffness 400, damping 28` | buttons, toggles, most interface motion |
| Gentle | `stiffness 200, damping 26` | modals, drawers, larger surfaces |
| Bouncy | `stiffness 500, damping 16` | one playful accent per page, at most |

Damping below about 15 oscillates visibly. That is a toy, not an interface. Springs beat durations
for anything interruptible (drag, rapid toggling) because they resolve from wherever they were
instead of restarting.

---

## Choreography

- **One focal point per moment.** If three things animate at once with equal weight, the eye picks
  none of them.
- **Stagger 40–80 ms** between siblings. Under 30 ms reads as simultaneous; over 120 ms reads as
  slow. Keep the total under ~500 ms: at 12 items a 60 ms stagger already costs 720 ms, so either
  drop the stagger or animate only the items in view.
- **Direction should match causality.** A dropdown grows from its trigger, a drawer comes from the
  edge it lives on, a toast enters from the corner it will occupy. Motion that arrives from nowhere
  is decoration.
- **Distance: 8–24 px is a reveal.** Past 40 px it is a journey and needs a reason.
- **Never animate a whole page on load.** Animate what is above the fold, then stop.

---

## What to animate

| Cheap (compositor) | Expensive (layout or paint) |
| --- | --- |
| `transform`: x, y, scale, rotate | `width`, `height`, `top`, `left`, `margin`, `padding` |
| `opacity` | `box-shadow`, `background-position`, `filter: blur` on large areas |

To animate size, scale a wrapper and counter-scale its content, or use a FLIP technique (Framer
Motion's `layout` prop, GSAP's `Flip` plugin). Animating `height` directly on anything larger than a
list row will show up on a mid-range phone.

Hover-scaling a card that contains text resamples the text and makes it blur. Scale the shadow and
the background, translate the card a couple of pixels, and leave the type alone.

---

## Personality

Pick one column and hold it across the entire surface. Mixed personalities are what "templated"
actually looks like.

| | Professional / SaaS | Editorial / luxury | Playful / consumer | Utility / dense |
| --- | --- | --- | --- | --- |
| Duration | 200–300 ms | 500–800 ms | 250–400 ms | 100–150 ms |
| Easing | ease-out, no bounce | slow ease-out | spring, light bounce | ease-out |
| Distance | 8–16 px | 24–40 px | 16–32 px | 4–8 px |
| Stagger | 50 ms | 90 ms | 40 ms | none |
| Scroll | reveal once | scrubbed, pinned | reveal once | none |

Ask which one the design is before writing the first transition. If the answer is not obvious, that
is a direction problem, not a motion problem: settle it with **ui-ux-pro-max** first.

---

## Reduced motion is a design, not a switch

`prefers-reduced-motion: reduce` does not mean "no feedback". It means no vestibular triggers:
no large travel, no parallax, no continuous loops, no scrubbing.

Keep the state change legible and drop the movement:

| Normal | Reduced |
| --- | --- |
| slide up 24 px + fade | fade only, same duration |
| scroll-scrubbed sequence | jump to the end state at the trigger point |
| looping ambient 3D | render one frame, then stop the loop |
| shared-element magic-move | cross-fade in place |

A modal that appears with no transition at all is worse than one that cross-fades in 120 ms. Shorten
and flatten; do not delete.

---

## Before calling it done

1. Does something actually change? If not, remove the animation.
2. Is the duration in the right band for the distance travelled?
3. Entering eases out, exiting eases in, scrubbed is linear?
4. Is the exit shorter than the entrance?
5. Transform and opacity only, or a stated reason otherwise?
6. One focal point, and total stagger under half a second?
7. Is there a designed reduced-motion path, not just a disabled one?
8. Does it still hold up with the CPU throttled 4x, and on a second visit when the novelty is gone?

Point 8 is the one that catches most of it. Motion is judged once by a new visitor and a hundred
times by a returning one. Build for the hundredth view.

---

## Tells of amateur motion

- Everything on the page fades in on scroll, including content that was already visible.
- The same 0.5 s ease applied to every element regardless of size.
- Bounce on a form control.
- A permanently pulsing CTA competing with the content it is supposed to lead to.
- An animation the user has to wait out before they can act.
- A 60-item list with a stagger on it.
- Hover states that move an element far enough that the pointer leaves it and it flickers.

---

Deeper treatment of motion principles: [LottieFiles/motion-design-skill](https://github.com/lottiefiles/motion-design-skill) (MIT).
