import { storiesOf } from '@storybook/vue'
import Map from '../Map'

const components = {
  'shops-map': Map
}

storiesOf('Map', module)
  .add('map with shop markers centered on the canton Fribourg', () => {
    return {
      components,
      template: '<shops-map :center="center" :zoom="zoom"/>',
      data: () => ({
        center: [46.718852, 7.097669],
        zoom: 11
      })
    }
  })
