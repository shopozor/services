import { configure } from '@storybook/vue';

// automatically import all files ending in *.stories.js
configure([
  require.context('../components', true, /\.stories\.js$/),
  require.context('../layouts', true, /\.stories\.js$/),
  require.context('../pages', true, /\.stories\.js$/)
], module);
