import { storiesOf } from '@storybook/vue'
// import { action } from '@storybook/addon-actions'

import Map from './Map'

storiesOf('Map', module)
  .add('default', () => {
    return {
      components: {
        'my-map': Map
      },
      template: '<my-map/>'
    }
  })
