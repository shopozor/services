import { createLocalVue, mount, shallowMount } from '@vue/test-utils'
import { LMap, LMarker, LTileLayer } from 'vue2-leaflet'
// eslint-disable-next-line no-unused-vars
import { GestureHandling } from 'leaflet-gesture-handling'
import ShopCard from '../ShopCard'
import Map from '../Map'
import ShopMarker from '../ShopMarker'
import ShopsData from '~fixtures/Consumer/Shops'

function getLocalVue () {
  const localVue = createLocalVue()
  localVue.component('l-map', LMap)
  localVue.component('l-tile-layer', LTileLayer)
  localVue.component('l-marker', LMarker)
  return localVue
}

function getMapComponentOptions (localVue, center, zoom, isLoading, data = null) {
  return {
    data,
    localVue,
    mocks: {
      $apollo: {
        queries: {
          shops: {
            loading: isLoading
          }
        }
      },
      $i18n: {
        t: () => {}
      }
    },
    propsData: {
      center,
      zoom
    }
  }
}

describe('Map', () => {
  const center = [46.718852, 7.097669]
  const zoom = 11
  const localVue = getLocalVue()

  it('is initialized with no shop description popup', () => {
    const wrapper = shallowMount(Map, getMapComponentOptions(localVue, center, zoom, false))
    expect(wrapper.vm.shop).toBeUndefined()
  })

  it('indicates loading shops', async () => {
    // Given I have a loading map
    const wrapper = mount(Map, getMapComponentOptions(localVue, center, zoom, true))

    // Then it is overlayed by a loading spinner or something equivalent
    await localVue.nextTick()
    const overlayElement = wrapper.find('.vld-overlay')
    expect(overlayElement.isVisible()).toBeTruthy()
  })

  it('is initialized with gesture handling', () => {
    // Given I have a loaded map
    const wrapper = mount(Map, getMapComponentOptions(localVue, center, zoom, false))

    // Then the gesture handling is enabled
    const leafletMap = wrapper.find('.vue2leaflet-map')
    const attributes = leafletMap.attributes()
    const expectedGestureHandlingAttributes = ['data-gesture-handling-touch-content', 'data-gesture-handling-scroll-content']
    const hasGestureHandling = expectedGestureHandlingAttributes.some(r => Object.keys(attributes).includes(r))
    expect(hasGestureHandling).toBeTruthy()
  })

  it('does not show zoom control', () => {
    const wrapper = mount(Map, getMapComponentOptions(localVue, center, zoom, false))
    const zoomControl = wrapper.find('.leaflet-control-zoom')
    expect(zoomControl.exists()).toBeFalsy()
  })

  it('displays the selected shop description', () => {
    // Given I have shops data and am not loading server data
    const data = () => ({
      shops: ShopsData.data.shops
    })
    const options = getMapComponentOptions(localVue, center, zoom, false, data)
    const wrapper = mount(Map, options)
    expect(wrapper.vm.shop).toBeUndefined()

    // When a child marker emits the display-description event
    const expectedShop = ShopsData.data.shops[0]
    const marker = wrapper.find(ShopMarker)
    marker.vm.$emit('display-description', expectedShop.id)

    // Then a shop is selected to display its description
    expect(wrapper.vm.shop).toBe(expectedShop)
  })

  it('clears shop description popup upon clicking the map', () => {
    // Given I have a shop selected for description
    const data = () => ({
      shops: ShopsData.data.shops,
      shop: ShopsData.data.shops[0]
    })
    const options = getMapComponentOptions(localVue, center, zoom, false, data)
    const wrapper = mount(Map, options)
    expect(wrapper.vm.shop).toBeDefined()

    // When the shop card emits the close event
    const shopCard = wrapper.find(ShopCard)
    shopCard.vm.$emit('close')

    // Then I have no shop selected anymore
    expect(wrapper.vm.shop).toBeUndefined()
  })
})
