const path = require('path')
const pkg = require('./package')

module.exports = {
  mode: 'universal',

  env: {
    GRAPHQL_API: process.env.GRAPHQL_API || 'http://localhost:8080/v1/graphql/'
  },

  /*
  ** Headers of the page
  */
  head: {
    title: pkg.name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
  ],

  /*
  ** Plugins to load before mounting the App
  */
  // TODO: we need tailwindcss plugin!
  plugins: [
    { src: '~plugins/errorHandling.js' },
    { src: '~plugins/leaflet.js', mode: 'client' }
  ],

  buildModules: [
    '@nuxtjs/tailwindcss'
  ],

  /*
  ** Nuxt.js modules
  */
  modules: ['@nuxtjs/apollo', 'nuxt-purgecss'],

  purgeCSS: {},

  // Give apollo module options
  apollo: {
    tokenExpires: 10, // optional, default: 7 (days)
    includeNodeModules: true, // optional, default: false (this includes graphql-tag for node_modules folder)
    authenticationType: 'Basic', // optional, default: 'Bearer'
    // optional
    // errorHandler (error) {
    //   console.log('%cError', 'background: red; color: white; padding: 2px 4px; border-radius: 3px; font-weight: bold;', error.message)
    // },
    // required
    clientConfigs: {
      default: '~/apollo/clientConfig.js'
    }
  },

  /*
  ** Build configuration
  */
  build: {
    extractCSS: true,
    postcss: {
      // Add plugin names as key and arguments as value
      // Install them before as dependencies with npm or yarn
      plugins: {
        // Disable a plugin by passing false as value
        // 'postcss-url': false,
        // 'postcss-nested': {},
        // 'postcss-responsive-type': {},
        // 'postcss-hexrgba': {}
      },
      preset: {
        // Change the postcss-preset-env settings
        autoprefixer: {
          grid: true
        }
      }
    },

    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
      config.resolve.alias['~graphql'] = path.resolve(__dirname, '../../shared/graphql/')
    }
  }
}
