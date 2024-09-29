/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './public/**/*.html',
    './src/**/*.{vue,js,ts,jsx,tsx}', // Ensure this line is present
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')], // Make sure DaisyUI is included here
}
