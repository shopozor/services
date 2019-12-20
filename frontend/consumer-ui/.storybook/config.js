import apolloStorybookDecorator from 'apollo-storybook-vue'
import { configure, addDecorator, addParameters } from '@storybook/vue'
import { INITIAL_VIEWPORTS } from '@storybook/addon-viewport'
import Vue from 'vue'
import VueI18n from 'vue-i18n'

import typeDefs from './schema/typeDefinitions'
import mocks from './schema/mocks'

import '../plugins/errorHandling'
import '../plugins/leaflet'

Vue.use(VueI18n)

// cf. https://github.com/storybookjs/storybook/tree/master/addons/viewport
addParameters({
  viewport: {
    viewports: INITIAL_VIEWPORTS,
    // TODO: this does not seem to be working!
    defaultViewport: 'mobile'
  },
})

addDecorator(
  apolloStorybookDecorator({
    typeDefs,
    mocks,
    Vue,
  })
)

configure([
  require.context('../components', true, /\.stories\.js$/),
  require.context('../layouts', true, /\.stories\.js$/),
  require.context('../pages', true, /\.stories\.js$/)
 ], module)
