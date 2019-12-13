import apolloStorybookDecorator from "apollo-storybook-vue"
import { configure, addDecorator } from '@storybook/vue'
import Vue from 'vue'

import typeDefs from './schema/typeDefinitions'
import mocks from './schema/mocks'

import '../plugins/errorHandling'
import '../plugins/leaflet'

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
