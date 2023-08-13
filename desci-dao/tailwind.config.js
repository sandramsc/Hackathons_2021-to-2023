/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    daisyui: {
      themes: [
        'emerald'
      ],
    },
    screens: {
      'xl': { 'max': '1279px' },
      // => @media (max-width: 1279px) { ... }
      'lg': { 'max': '1023px' },
      // => @media (max-width: 1023px) { ... }
      'md': { 'max': '767px' },
      // => @media (max-width: 767px) { ... }
      'sm': { 'max': '639px' },
      // => @media (max-width: 639px) { ... }
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['serif'],
    },
    extend: {
      spacing: {
        128: '32rem',
        144: '36rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
      colors: {
        white: '#fff',
        blue: "#04d9ff",
        primary: "#191d26",
        primaryColor: "#00040f",
        secondaryColor: "#00f6ff",
        secondaryColor_green: '#c2f70f',
        primaryColor_orange: '#ff9f00',
        secondaryColor_orange: '#fe7a15',
      },
    },
    extend: {},
  },
  plugins: [require("daisyui")],
}
