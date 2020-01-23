const path = require('path')
const tailwindcss = require('tailwindcss')
const webpack = require('webpack')

module.exports = async ({ config, mode }) => {

  config.module.rules.push({
    test: /\.(graphql|gql)$/,
    exclude: /node_modules/,
    use: ['graphql-tag/loader'],
    include: [path.resolve(__dirname, '../'), path.resolve(__dirname, '../../../shared/graphql/')],
  })

  config.module.rules.push({
    test: /\.css$/,
    use: [
      {
        loader: "postcss-loader",
        options: {
          ident: "postcss",
          plugins: [
            require("postcss-import"),
            tailwindcss('./tailwind.config.js'),
            require("autoprefixer")
          ]
        }
      }
    ],
    include: path.resolve(__dirname, "../")
  })

  config.plugins.push(
    new webpack.DefinePlugin({
      'process.env.ASSETS_API': JSON.stringify(process.env.ASSETS_API || 'http://localhost:9001/')
    })
  )

  config.resolve.alias['~assets'] = path.resolve(__dirname, '../assets/')
  config.resolve.alias['~'] = path.resolve(__dirname, '../')
  config.resolve.alias['~shared'] = path.resolve(__dirname, '../../../shared/')
  config.resolve.alias['~graphql'] = path.resolve(__dirname, '../../../shared/graphql/')
  config.resolve.alias['~fixtures'] = path.resolve(__dirname, '../../../shared/fixtures/graphql/responses/')

  config.resolve.extensions.push('.gql', '.graphql')

  return config
}