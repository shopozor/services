import { storiesOf } from '@storybook/vue'

import ShopozorFooter from '../Footer'

const components = {
  ShopozorFooter
}

storiesOf('Footer', module)
  .add('Footer', () => {
    return {
      components,
      template: '<shopozor-footer />'
    }
  })
