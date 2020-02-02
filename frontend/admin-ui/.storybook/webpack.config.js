const path = require("path");

module.exports = ({ config }) => {
  config.module.rules.push({
    test: /\.(scss|sass)$/,
    use: ["style-loader", "css-loader", "sass-loader"],
    include: path.resolve(__dirname, "../")
  });
  config.module.rules.push({
    test: /\.stories\.js?$/,
    use: [
      {
        loader: require.resolve("@storybook/source-loader")
      }
    ],
    enforce: "pre"
  });
  return config;
};
