import { defineConfig } from "astro/config";
import vercel from "@astrojs/vercel";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  adapter: vercel(),
  // Astro y Tailwind pueden resolver versiones distintas de Vite en el árbol npm.
  // @ts-expect-error La incompatibilidad solo afecta a los tipos duplicados de Vite.
  vite: { plugins: [tailwindcss()] },
});
