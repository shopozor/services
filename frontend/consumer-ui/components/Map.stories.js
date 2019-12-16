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
  // TODO: need to test what happens in case there is no data
  // TODO: by default --> max zoom out to see the whole switzerland
  // TODO: later: if a consumer has an account, center on her location
