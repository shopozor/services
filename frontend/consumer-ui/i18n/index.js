module.exports = {
  locales: [
    {
      code: 'fr',
      iso: 'fr-CH',
      name: 'Français',
      file: 'fr.js'
    }
  ],
  defaultLocale: 'fr',
  seo: false,
  lazy: true,
  detectBrowserLanguage: {
    cookieKey: 'redirected',
    useCookie: true
  },
  langDir: 'i18n/',
  parsePages: false,
  // pages: {
  //   about: {
  //     de: '/ueber-uns/',
  //     en: '/about-us/'
  //   },
  //   work: {
  //     de: '/referenzen/',
  //     en: '/work/'
  //   },
  //   legal: {
  //     de: '/impressum/',
  //     en: '/legal/'
  //   },
  //   disclaimer: {
  //     de: '/haftungsausschluss/',
  //     en: '/disclaimer/'
  //   },
  //   privacy: {
  //     de: '/datenschutz/',
  //     en: '/privacy/'
  //   }
  // },
  vueI18n: {
    fallbackLocale: 'fr'
  }
}
