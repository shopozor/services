module.exports = {
  root: true,

  parserOptions: {
    parser: 'babel-eslint',
    sourceType: 'module'
  },

  env: {
    browser: true
  },

  extends: [
    // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
    // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
    '@nuxtjs',
    'plugin:chai-friendly/recommended',
    'plugin:cypress/recommended',
    'plugin:vue/essential',
    'plugin:jest/recommended'
  ],

  // required to lint *.vue files
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

    'import/first': 'off',
    'import/named': 'error',
    'import/namespace': 'error',
    'import/default': 'error',
    'import/export': 'error',
    'import/extensions': 'off',
    'import/no-unresolved': 'off',
    'import/no-extraneous-dependencies': 'off',
    'prefer-promise-reject-errors': 'off',

    "cucumber/async-then": 2,
    "cucumber/expression-type": 2,
    "cucumber/no-restricted-tags": [2, "wip", "broken", "foo"],
    "cucumber/no-arrow-functions": 2,

    // allow debugger during development only
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
  }
}
