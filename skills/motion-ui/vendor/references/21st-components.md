# 21st.dev — Sourcing & Fallback Recipes

The skill sources professional components in **hybrid** mode:

1. **Live (preferred):** if the 21st.dev **Magic MCP** is connected, use it to fetch/generate
   real components. Discover it with `ToolSearch` (query: `21st magic component ui`). Tool names
   typically look like `mcp__*magic*__*` (e.g. component builder / inspiration / logo search).
   If present, call it with the user's request and adapt the returned code to the project's
   stack, Tailwind config, and `motion/react` import path.
2. **Fallback (always works):** if no Magic MCP is connected, build from the recipes below —
   21st.dev-style: Tailwind + Radix primitives where useful + `motion/react` for animation.

> Detecting Magic MCP: run a `ToolSearch` for `magic 21st component`. If zero relevant tools
> come back, announce "Magic MCP not detected — using built-in 21st-style patterns" and proceed
> with the fallback. Never block on the MCP.

---

## Fallback recipes (Tailwind + motion/react)

### Animated CTA button
```tsx
"use client";
import { motion } from "motion/react";
export function CTAButton({ children }: { children: React.ReactNode }) {
  return (
    <motion.button
      whileHover={{ scale: 1.03 }}
      whileTap={{ scale: 0.97 }}
      transition={{ type: "spring", stiffness: 400, damping: 22 }}
      className="rounded-xl bg-indigo-600 px-6 py-3 font-medium text-white shadow-lg shadow-indigo-600/25 transition-colors hover:bg-indigo-500"
    >
      {children}
    </motion.button>
  );
}
```

### Spotlight / gradient hero card
```tsx
"use client";
import { motion } from "motion/react";
export function HeroCard({ title, body }: { title: string; body: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-60px" }}
      transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
      className="relative overflow-hidden rounded-2xl border border-white/10 bg-gradient-to-b from-white/5 to-transparent p-8 backdrop-blur"
    >
      <div className="pointer-events-none absolute -top-24 left-1/2 h-48 w-48 -translate-x-1/2 rounded-full bg-indigo-500/30 blur-3xl" />
      <h3 className="text-xl font-semibold text-white">{title}</h3>
      <p className="mt-2 text-sm text-white/60">{body}</p>
    </motion.div>
  );
}
```

### Staggered feature grid
```tsx
"use client";
import { motion } from "motion/react";
const container = { hidden: {}, show: { transition: { staggerChildren: 0.08 } } };
const item = { hidden: { opacity: 0, y: 20 }, show: { opacity: 1, y: 0 } };
export function FeatureGrid({ features }: { features: { title: string; desc: string }[] }) {
  return (
    <motion.div
      variants={container} initial="hidden" whileInView="show" viewport={{ once: true }}
      className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3"
    >
      {features.map((f) => (
        <motion.div key={f.title} variants={item}
          className="rounded-xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900">
          <h4 className="font-semibold">{f.title}</h4>
          <p className="mt-1 text-sm text-zinc-500">{f.desc}</p>
        </motion.div>
      ))}
    </motion.div>
  );
}
```

### Animated modal (AnimatePresence)
```tsx
"use client";
import { AnimatePresence, motion } from "motion/react";
export function Modal({ open, onClose, children }: { open: boolean; onClose: () => void; children: React.ReactNode }) {
  return (
    <AnimatePresence>
      {open && (
        <motion.div className="fixed inset-0 z-50 grid place-items-center bg-black/50"
          initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} onClick={onClose}>
          <motion.div onClick={(e) => e.stopPropagation()}
            initial={{ opacity: 0, scale: 0.95, y: 10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 10 }}
            transition={{ duration: 0.2 }}
            className="w-full max-w-md rounded-2xl bg-white p-6 shadow-2xl dark:bg-zinc-900">
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

## Quality bar (apply to every component, Magic-sourced or fallback)
- Respects `prefers-reduced-motion` (see motion-patterns.md §Accessibility).
- Dark-mode aware (`dark:` variants) when the project uses Tailwind dark mode.
- Semantic HTML + keyboard accessible (real `<button>`, focus rings, `aria-*` on modals).
- Animates only transform/opacity. No layout-thrash.
- Matches the project's existing token/color system — read tailwind.config + globals before inventing colors.

## Composing with sibling skills
- Pull color palettes, font pairings, and style direction from the **ui-ux-pro-max** skill.
- Pull shadcn/ui component scaffolds from the **ui-styling** skill, then layer motion on top.
