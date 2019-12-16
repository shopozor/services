import { storiesOf } from '@storybook/vue'

import ShopCard from './ShopCard'

const components = {
  'shop-card': ShopCard
}

storiesOf('ShopCard', module)
  .add('Map marker popup', () => {
    return {
      components,
      template: '<shop-card :name="name" :description="description"/>',
      data: () => ({
        name: 'Budzonnerie d\'Onnens',
        description: 'Obtenir une description fake de nos fixtures'
      })
    }
  })
