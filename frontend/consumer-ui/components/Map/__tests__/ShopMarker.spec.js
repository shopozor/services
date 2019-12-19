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
    const wrapper = shallowMount(ShopMarker, {
      localVue,
      propsData: {
        shop: ShopsData.data.shops[0]
      }
    })
    // TODO: is there a way to emit the click event without MOUNTING the component?
    //       here we can only shallowMount
    wrapper.vm.onClick()
    const emitted = wrapper.emitted()
    const displayDescriptionEvent = emitted['display-description']
    expect(displayDescriptionEvent).toBeTruthy()
    expect(displayDescriptionEvent[0]).toEqual([1])
  })
})
