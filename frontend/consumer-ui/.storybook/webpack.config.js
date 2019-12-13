const path = require('path')

module.exports = async ({ config, mode }) => {

  config.module.rules.push({
    test: /\.(graphql|gql)$/,
    exclude: /node_modules/,
    use: ['graphql-tag/loader'],
    include: [path.resolve(__dirname, '../'), path.resolve(__dirname, '../../../shared/graphql/')],
  })

  config.resolve.alias = {
    ...config.resolve.alias,
    '~': path.resolve(__dirname, '../'),
    '~graphql': path.resolve(__dirname, '../../../shared/graphql/')
  }

  config.resolve.extensions.push('.gql', '.graphql')

  return config
}