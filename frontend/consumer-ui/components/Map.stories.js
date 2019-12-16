import { storiesOf } from '@storybook/vue'
import Map from './Map'

const components = {
  'shops-map': Map
}

storiesOf('Map', module)
  .add('map with shop markers', () => {
    return {
      components,
      template: '<shops-map/>'
    }
  })
