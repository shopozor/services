const path = require('path')
const tailwindcss = require('tailwindcss')

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

  config.resolve.alias['~'] = path.resolve(__dirname, '../')
  config.resolve.alias['~graphql'] = path.resolve(__dirname, '../../../shared/graphql/')
  config.resolve.alias['~fixtures'] = path.resolve(__dirname, '../../../shared/fixtures/graphql/responses/')

  config.resolve.extensions.push('.gql', '.graphql')

  return config
}