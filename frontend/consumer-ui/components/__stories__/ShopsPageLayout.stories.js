import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import ShopozorHeader from '../Header'
import ShopozorFooter from '../Footer'

const components = {
  ShopozorFooter,
  ShopozorHeader
}

export const methods = {
  onLogin: action('onLogin')
}

storiesOf('Shops page layout', module)
  .add('Footer', () => {
    return {
      components,
      template: '<shopozor-footer />'
    }
  })
  .add('Header', () => {
    return {
      components,
      template: '<shopozor-header @login="onLogin"/>',
      methods
    }
  })
