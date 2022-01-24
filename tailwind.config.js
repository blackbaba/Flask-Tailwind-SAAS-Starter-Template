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
      rose: colors.rose,
      red: colors.red,
      flasky: colors.sky,
      // flasky: {
      //   50: '#f1f5f9',
      //   100: '#94a3b8',
      //   200: '#64748b',
      //   300: '#334155',
      //   400: '#1e293b',
      //   500: '#0f172a',
      //   600: '#0f172a',
      //   700: '#0f172a',
      //   800: '#0f172a',
      //   900: '#0f172a',
      // }  // Set brand color here
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
  ]
}
