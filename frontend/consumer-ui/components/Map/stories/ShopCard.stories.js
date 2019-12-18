import { storiesOf } from '@storybook/vue'
import ShopCard from '../ShopCard'
import ShopsData from '~fixtures/Consumer/Shops'

const components = {
  'shop-card': ShopCard
}

const shop = ShopsData.data.shops[0]

storiesOf('ShopCard', module)
  .add('Map marker popup', () => {
    return {
      components,
      template: '<shop-card :shop="shop"/>',
      data: () => ({
        shop
      })
    }
  })
