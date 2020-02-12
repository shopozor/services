module.exports = {
  // noStackTrace: true,
  // bail: true,
  // cache: false,
  // verbose: true,
  // watch: true,
  coverageDirectory: '<rootDir>/test/jest/coverage',
  collectCoverageFrom: [
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
  moduleFileExtensions: [
    'js',
    'json'
  ],
  testMatch: [
    '<rootDir>/**/__tests__/*.spec.js'
  ],
  moduleNameMapper: {
    '.+\\.(css|styl|less|sass|scss|svg|png|jpg|ttf|woff|woff2)$': 'jest-transform-stub',
    '^src/(.*)$': '<rootDir>/src/$1'
  },
  transform: {
    '.*\\.js$': 'babel-jest'
  }
}
