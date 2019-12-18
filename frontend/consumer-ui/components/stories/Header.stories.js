import { storiesOf } from '@storybook/vue'

import ShopozorHeader from '../Header'

const components = {
  ShopozorHeader
}

storiesOf('Header', module)
  .add('Header', () => {
    return {
      components,
      template: '<shopozor-header />'
    }
  })
