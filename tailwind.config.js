const colors = require('tailwindcss/colors')

module.exports = {
  content: ["./app/templates/**/*.html"],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      black: colors.black,
      white: colors.white,
      gray: colors.gray,
      error: colors.rose,
      danger: colors.rose,
      message: colors.green,
      warning: colors.yellow,
      emerald: colors.emerald,
      flasky: colors.emerald  // Set brand color here
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
  ],
}
