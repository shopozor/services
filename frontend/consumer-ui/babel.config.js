const fs = require('fs-extra')
let extend

/**
 * The .babelrc file has been created to assist Jest for transpiling.
 * You should keep your application's babel rules in this file.
 */

if (fs.existsSync('./.babelrc')) {
  extend = './.babelrc'
}

module.exports = api => ({
  presets: [
    '@vue/app'
  ],
  ...(api.env('test') && { plugins: ['require-context-hook'] }),
  extends: extend
})
