const defaultTheme = require("tailwindcss/defaultTheme");
module.exports = {
  purge: { content: ["./public/**/*.html", "./src/**/*.vue"] },
  darkMode: false, // or 'media' or 'class'
  theme: {
    screens: {
      xxs: "375px",
      xs: "480px",
      ...defaultTheme.screens,
    },
    extend: {
      inset: {
        "17": "68px",
        "26": "104px",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms"), require("tailwind-hamburgers")],
};
