module.exports = {
  "overrides": [{
    "files": [ "*.spec.js", "*.commands.js" ],
    "rules": {
      "jest/no-standalone-expect": 0,
      "jest/valid-expect": 0
    }
  }]
}