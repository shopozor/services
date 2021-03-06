import apolloStorybookDecorator from 'apollo-storybook-vue'
import { configure, addDecorator, addParameters } from '@storybook/vue'
import {action} from '@storybook/addon-actions'
import { INITIAL_VIEWPORTS } from '@storybook/addon-viewport'
import Vue from 'vue'
import VueI18n from 'vue-i18n'
import fr from '~/i18n/fr'
import '~/plugins/errorHandling'
import '~/plugins/leaflet'
import viewports from '~shared/storybook/viewports'

import typeDefs from './schema/schema.graphql'
import mocks from './schema/mocks'

import "~assets/css/tailwind.css"

Vue.use(VueI18n)

Vue.component('NuxtLink', {
  props:   ['to'],
  methods: {
    log() {
      action('link target')(this.to)
    },
  },
  template: '<div @click="log()"><slot>NuxtLink</slot></div>',
})

addParameters({
  viewport: {
    viewports: {
      ...viewports,
      ...INITIAL_VIEWPORTS
    },
    defaultViewport: 'sm'
  },
})

const i18n = new VueI18n({
  locale: 'fr',
  messages: {
    fr
  }
})

addDecorator(() => ({
  template: '<story/>',
  i18n
}))

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