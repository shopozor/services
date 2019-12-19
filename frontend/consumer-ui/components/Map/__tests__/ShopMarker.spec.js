import { createLocalVue, shallowMount } from '@vue/test-utils'
import { LMarker } from 'vue2-leaflet'
import ShopMarker from '../ShopMarker'
import ShopsData from '~fixtures/Consumer/Shops'

function getLocalVue () {
  const localVue = createLocalVue()
  localVue.component('l-marker', LMarker)
  return localVue
}

describe('ShopMarker', () => {
  const localVue = getLocalVue()

  it('emits display-description with shop id event upon click', () => {
    // Given I have a shop marker
    const wrapper = shallowMount(ShopMarker, {
      localVue,
      propsData: {
        shop: ShopsData.data.shops[0]
      }
    })

    // When I click on it
    // Because we can't mount the component completely (we need to shallow mount),
    // there is no way to trigger the click event with something like
    //   const marker = wrapper.find(LMarker)
    //   marker.trigger('click')
    // Therefore we call the onClick method directly
    wrapper.vm.onClick()

    // Then the display-description event is emitted with the corresponding shop's id
    const emitted = wrapper.emitted()
    const displayDescriptionEvent = emitted['display-description']
    expect(displayDescriptionEvent).toBeTruthy()
    expect(displayDescriptionEvent[0]).toEqual([1])
  })
})
