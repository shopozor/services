import { createLocalVue, mount, shallowMount } from '@vue/test-utils'
import { LMap, LMarker, LTileLayer } from 'vue2-leaflet'
// eslint-disable-next-line no-unused-vars
import { GestureHandling } from 'leaflet-gesture-handling'
import Map from '../Map'

function getLocalVue () {
  const localVue = createLocalVue()
  localVue.component('l-map', LMap)
  localVue.component('l-tile-layer', LTileLayer)
  localVue.component('l-marker', LMarker)
  return localVue
}

describe('Map', () => {
  const center = [46.718852, 7.097669]
  const zoom = 11
  const localVue = getLocalVue()

  it('renders spinner when loading shops', async () => {
    const wrapper = mount(Map, {
      localVue,
      propsData: {
        center,
        zoom
      },
      mocks: {
        $apollo: {
          queries: {
            shops: {
              loading: true
            }
          }
        }
      }
    })
    await localVue.nextTick()
    const overlayElement = wrapper.find('.vld-overlay')
    expect(overlayElement.isVisible()).toBeTruthy()
  })

  // TODO: get rid of this test in the very near future
  it('is initialized with gesture handling', () => {
    const wrapper = shallowMount(Map, {
      localVue,
      mocks: {
        $apollo: {
          queries: {
            shops: {
              loading: false
            }
          }
        }
      },
      propsData: {
        center,
        zoom
      }
    })
    expect(wrapper.vm.options.gestureHandling).toBeTruthy()
  })

  // TODO: transform this test into a cypress test, maybe it'll work
  /* it('has gesture handling enabled', async () => {
    const wrapper = mount(Map, {
      attachToDocument: true,
      localVue,
      mocks: {
        $apollo: {
          queries: {
            shops: {
              loading: false
            }
          }
        }
      },
      propsData: {
        center,
        zoom
      }
    })
    // const map = wrapper.find('.vue2leaflet-map')
    window.dispatchEvent(new CustomEvent('scroll'))
    await localVue.nextTick()
    expect(wrapper.element).toMatchSnapshot()
    wrapper.destroy()
  }) */

  /*
  it('does not show zoom control')

  it('is initialized with no shop description popup')

  it('clears shop description popup upon clicking the map')

  // TODO: test displaying of the description
  */
})
