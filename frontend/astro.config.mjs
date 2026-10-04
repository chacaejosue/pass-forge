import { defineConfig } from "astro/config";
import vercel from "@astrojs/vercel";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  adapter: vercel(),
  vite: {
    // Astro y Tailwind pueden resolver versiones distintas de Vite en el árbol npm.
    // @ts-ignore La incompatibilidad solo afecta a los tipos duplicados de Vite.
    plugins: [tailwindcss()],
    server: { proxy: { "/api": "http://127.0.0.1:5000" } },
  },
});
