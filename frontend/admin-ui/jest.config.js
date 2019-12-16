module.exports = {
  setupFilesAfterEnv: [
    '<rootDir>/test/jest/jest.setup.js'
  ],
  // noStackTrace: true,
  // bail: true,
  // cache: false,
  // verbose: true,
  // watch: true,
  coverageDirectory: '<rootDir>/test/jest/coverage',
  collectCoverageFrom: [
    '<rootDir>/src/**/*.vue',
    '<rootDir>/src/**/*.js'
  ],
  coverageThreshold: {
    global: {
    //  branches: 50,
    //  functions: 50,
    //  lines: 50,
    //  statements: 50
    }
  },
  testMatch: [
    '<rootDir>/test/jest/__tests__/**/*.spec.js',
    '<rootDir>/test/jest/__tests__/**/*.test.js',
    '<rootDir>/test/snapshots/**/*.spec.js',
    '<rootDir>/src/**/__tests__/*_jest.spec.js'
  ],
  moduleNameMapper: {
    '^vue$': '<rootDir>/node_modules/vue/dist/vue.common.js',
    '^test-utils$': '<rootDir>/node_modules/@vue/test-utils/dist/vue-test-utils.js',
    '^quasar$': '<rootDir>/node_modules/quasar/dist/quasar.common.js',
    '^~/(.*)$': '<rootDir>/$1',
    '^src/(.*)$': '<rootDir>/src/$1',
    '.*css$': '<rootDir>/test/jest/utils/stub.css'
  },
  transform: {
    '\\.(gql|graphql)$': '@jagi/jest-transform-graphql'
  },
  transformIgnorePatterns: [
    '<rootDir>/node_modules/(?!quasar/lang)',
    '/node_modules/(?!(@storybook/.*\\.vue$))'
  ],
  setupFiles: [
    '<rootDir>/test/register-context.js'
  ]
}
