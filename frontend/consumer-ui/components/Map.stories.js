import { storiesOf } from '@storybook/vue'
// import { action } from '@storybook/addon-actions'

import Map from './Map'

const components = {
  'shops-map': Map
}

storiesOf('Map', module)
  .add('empty map', () => {
    return {
      components,
      template: '<shops-map/>'
    }
  })
  .add('map with one single marker')
  // Place one shop marker to see what that looks like
  // Get shops from database --> place shops markers
  // Upon clicking a shop marker, the shop card pops up
