const fs = require('fs-extra')
let extend

/**
 * The .babelrc file has been created to assist Jest for transpiling.
 * You should keep your application's babel rules in this file.
 */

if (fs.existsSync('./.babelrc')) {
  extend = './.babelrc'
}

module.exports = api => {
  api.cache(true)
  return {
    presets: [
      '@quasar/babel-preset-app'
    ],
    extends: extend
  }
}
