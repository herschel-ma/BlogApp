// var BundleTracker = require("webpack-bundle-tracker");
module.exports = {
  publicPath:
    process.env.NODE_ENV !== "production"
      ? "http://localhost:8080/"
      : "/static/dist",
  outputDir: "../static/dist/",
  indexPath: "../../templates/base-vue.html",
  runtimeCompiler: true,

  chainWebpack: (config) => {
    config.optimization.splitChunks(false);

    // config
    //   .plugin("BundleTracker")
    //   .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

    // config.output.filename("bundle.js");

    // config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public("http://localhost:8080")
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ "Access-Control-Allow-Origin": ["*"] })
      .writeToDisk((filePath) => filePath.endsWith("index.html"));
  },
};
