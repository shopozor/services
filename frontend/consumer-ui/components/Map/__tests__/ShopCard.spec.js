import { createLocalVue, shallowMount } from '@vue/test-utils'
import ShopCard from '../ShopCard'
import ShopsData from '~fixtures/Consumer/Shops'

function getComponentOptions (localVue) {
  return {
    propsData: {
      shop: ShopsData.data.shops[0]
    },
    localVue
  }
}

describe('ShopCard', () => {
  const localVue = createLocalVue()
  it('emits close event upon clicking the close button', () => {
    // Given the card is open
    const wrapper = shallowMount(ShopCard, getComponentOptions(localVue))

    // When I click the close button
    const closeBtn = wrapper.find('.cursor-pointer')
    closeBtn.trigger('click')

    // Then the close event is emitted
    expect(wrapper.emitted().close).toBeTruthy()
  })
})
