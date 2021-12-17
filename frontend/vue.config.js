var BundleTracker = require("webpack-bundle-tracker");
module.exports = {
  // publicPath: "http://127.0.0.1:8000/",
  publicPath: ".",
  outputDir: "./dist/",
  runtimeCompiler: true,

  chainWebpack: (config) => {
    config.optimization.splitChunks(false);

    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

    config.output.filename("bundle.js");

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public("http://127.0.0.1:8080")
      .host("127.0.0.1")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  },
};
