import { configure } from '@storybook/vue';

import '../plugins/errorHandling'
import '../plugins/leaflet'

configure([
  require.context('../components', true, /\.stories\.js$/),
  require.context('../layouts', true, /\.stories\.js$/),
  require.context('../pages', true, /\.stories\.js$/)
 ], module);
