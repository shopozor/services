import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import PreviewModal from '../PreviewModal'

const components = {
  PreviewModal
}

export const methods = {
  onClose: action('onClose')
}

storiesOf('Preview modal', module)
  .add('Modal content', () => {
    return {
      components,
      template: '<preview-modal @close="onClose"/>',
      methods
    }
  })
