// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  typescript: {
    typeCheck: true
  },

  css: ['~/assets/css/main.css', 'primevue/resources/themes/aura-light-green/theme.css', 'primeicons/primeicons.css'],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  modules: [
    "@sidebase/nuxt-auth",
    "nuxt-primevue",
    "@pinia/nuxt",
  ],
  primevue: {
    components: {
      include: ['Carousel', 'Tag', 'Button', 'Toast', 'ProgressSpinner', 'Message', 'Rating', 'Listbox', 'InputText', 'FloatLabel', 'SelectButton', 'TextArea', 'Calendar', 'InputNumber']
    }
  },
  auth: {
    baseURL: 'http://somativa-production.up.railway.app',
    provider: {
      type: 'local',
      endpoints: {
        signIn: { path: '/token/login', method: 'post' },
        signOut: { path: '/token/logout', method: 'post' },
        getSession: { path: '/custom-user', method: 'get' },
      },
      token: { signInResponseTokenPointer: '/auth_token', type: 'Token' },
      pages: { login: '/login' },
      sessionDataType: {
        results: 'Array'
      }
    }
  }
})