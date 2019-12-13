const path = require('path')

module.exports = async ({ config, mode }) => {

  config.module.rules.push({
    test: /\.(graphql|gql)$/,
    exclude: /node_modules/,
    use: ['graphql-tag/loader'],
    include: [path.resolve(__dirname, '../'), path.resolve(__dirname, '../../../shared/graphql/')],
  })

  config.resolve.alias['~'] = path.resolve(__dirname, '../')
  config.resolve.alias['~graphql'] = path.resolve(__dirname, '../../../shared/graphql/')
  config.resolve.alias['~fixtures'] = path.resolve(__dirname, '../../../shared/fixtures/graphql/responses/')

  config.resolve.extensions.push('.gql', '.graphql')

  return config
}