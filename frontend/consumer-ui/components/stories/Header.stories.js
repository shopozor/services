import { storiesOf } from '@storybook/vue'

import Header from '../Header'

const components = {
  'my-header': Header
}

storiesOf('Header', module)
  .add('Header', () => {
    return {
      components,
      template: '<my-header />'
    }
  })
