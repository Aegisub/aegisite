const autoprefixer = require('autoprefixer');
const purgecss = require('@fullhuman/postcss-purgecss');

module.exports = {
  plugins: [
    autoprefixer(),
    purgecss({
      content: [
        './layouts/**/*.html',
        './content/**/*.md',
        './assets/scss/components/{alerts,buttons,code,diagrams,syntax,search}.scss',
        './assets/scss/common/_dark.scss',
        './node_modules/bootstrap/scss/_dropdown.scss',
        './node_modules/katex/dist/katex.css',
      ],
      safelist: [
        'table',
        'thead',
        'tbody',
        'tr',
        'th',
        'td',
        'h5',
        'alert-link',
        'container-xxl',
        'container-fluid',
        'img-fluid',
        'figcaption',
      ],
    }),
  ],
}
