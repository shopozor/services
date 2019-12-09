module.exports = {
  collectCoverage: true,
  globals: {
    __DEV__: true
  },
  moduleFileExtensions: [
    'vue',
    'js',
    'json',
    'ts'
  ],
  projects: [
    '<rootDir>/frontend/admin-ui/jest.config.js',
    '<rootDir>/frontend/consumer-ui/jest.config.js'
  ],
  snapshotSerializers: [
    '<rootDir>/node_modules/jest-serializer-vue'
  ],
  transform: {
    '.*\\.vue$': 'vue-jest',
    '.*\\.js$': 'babel-jest',
    '.+\\.(css|styl|less|sass|scss|svg|png|jpg|ttf|woff|woff2)$': 'jest-transform-stub'
    // use these if NPM is being flaky
    // '.*\\.vue$': '<rootDir>/node_modules/@quasar/quasar-app-extension-testing-unit-jest/node_modules/vue-jest',
    // '.*\\.js$': '<rootDir>/node_modules/@quasar/quasar-app-extension-testing-unit-jest/node_modules/babel-jest'
  }
}
