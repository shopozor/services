import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import ShopozorHeader from '../Header'

const components = {
  ShopozorHeader
}

export const methods = {
  onLogin: action('onLogin')
}

storiesOf('Header', module)
  .add('Header', () => {
    return {
      components,
      template: '<shopozor-header @login="onLogin"/>',
      methods
    }
  })
