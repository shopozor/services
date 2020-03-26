const path = require('path')
const fs = require('fs-extra')

function getConfigurationByFile (file) {
  const pathToConfigFile = path.resolve('cypress', 'config', `${file}.json`)
  console.log('loading cypress config file: ', pathToConfigFile)
  return fs.readJson(pathToConfigFile)
}

exports.getConfiguration = function (config) {
  const file = config.env.configFile || 'integration'
  return getConfigurationByFile(file)
}
