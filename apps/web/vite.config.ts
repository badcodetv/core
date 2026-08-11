import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// @badcode/comic is consumed directly from TypeScript source via the workspace,
// so no pre-build step is needed for development.
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      // Generated program interfaces. Vite does not read tsconfig paths, so this
      // has to be stated twice; if you add a path mapping there, add it here.
      '@chain': fileURLToPath(new URL('../../chain', import.meta.url)),
    },
  },
  server: {
    port: 5173,
  },
})
