// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

import react from '@astrojs/react';

// https://astro.build/config
export default defineConfig({
  i18n: {
    defaultLocale: 'nl',
    locales: ['nl', 'en', 'de'],
    routing: {
      prefixDefaultLocale: true // Start with /nl for default, matching the [lang] folder structure
    }
  },

  vite: {
    plugins: [tailwindcss()]
  },

  integrations: [react()]
});