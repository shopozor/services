import { createLocalVue, shallowMount } from '@vue/test-utils'
import PreviewModal from '../PreviewModal'

describe('PreviewModal', () => {
  const localVue = createLocalVue()
  it('emits close event upon clicking the close button', () => {
    // Given the modal has popped up
    const wrapper = shallowMount(PreviewModal, { localVue })

    // When I click the close button
    const closeBtn = wrapper.find('.cursor-pointer')
    closeBtn.trigger('click')

    // Then the close event is emitted
    expect(wrapper.emitted().close).toBeTruthy()
  })
})
