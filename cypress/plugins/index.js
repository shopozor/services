// ***********************************************************
// This example plugins/index.js can be used to load plugins
//
// You can change the location of this file or turn off loading
// the plugins file with the 'pluginsFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/plugins-guide
// ***********************************************************

// This function is called when a project is opened or re-opened (e.g. due to
// the project's config changing)

const cucumber = require('cypress-cucumber-preprocessor').default

module.exports = (on, config) => {
  on('before:browser:launch', (browser = {}, args) => {
    if (process.env.NODE_ENV === 'development' && browser.name === 'chrome') {
      args.push('--remote-debugging-port=9222')
      console.log('DEBUG MODE ENABLED')
      return args
    }
  })
  on('file:preprocessor', cucumber())
}
