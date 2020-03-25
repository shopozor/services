module.exports = {
  root: true,

  parserOptions: {
    parser: 'babel-eslint',
    sourceType: 'module'
  },

  env: {
    browser: true,
    jest: true
  },

  extends: [
    '@nuxtjs',
    'plugin:chai-friendly/recommended',
    'plugin:cypress/recommended',
    'plugin:jest/recommended',
    'plugin:vue/recommended',
    'standard'
  ],

  plugins: [
    'chai-friendly',
    'cucumber',
    'cypress',
    'vue'
  ],

  globals: {
    'ga': true, // Google Analytics
    'cordova': true,
    '__statics': true,
    'process': true,
    'Capacitor': true,
    'chrome': true,
    'defineParameterType': true // cypress-cucumber-preprocessor
  },
  // add your custom rules here
  rules: {
    'no-console': 'off',
    'nuxt/no-cjs-in-config': 'off',
    // allow async-await
    'generator-star-spacing': 'off',
    // allow paren-less arrow functions
    'arrow-parens': 'off',
    'one-var': 'off',
    'no-trailing-spaces': 'error',

    'import/first': 'off',
    'import/named': 'error',
    'import/namespace': 'error',
    'import/default': 'error',
    'import/export': 'error',
    'import/extensions': 'off',
    'import/no-unresolved': 'off',
    'import/no-extraneous-dependencies': 'off',
    'prefer-promise-reject-errors': 'off',

    "cucumber/async-then": 'off',
    "cucumber/expression-type": 2,
    "cucumber/no-restricted-tags": [2, "current", "focus"],
    "cucumber/no-arrow-functions": 2,

    // allow debugger during development only
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
  },
  overrides: [{
    files: [ '*.md', '*.feature' ],
    rules: {
      'no-trailing-spaces': 'off',
    }
  }]
}
