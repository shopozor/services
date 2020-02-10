import { storiesOf } from '@storybook/vue'
import ShakingButton from './ShakingBtn.vue'
import ValidityIcon from './ValidityIcon.vue'
import InputWithValidation from './InputWithValidation.vue'
import CheckboxWithValidation from './CheckboxWithValidation.vue'

const components = {
  ShakingButton,
  ValidityIcon,
  InputWithValidation,
  CheckboxWithValidation
}

storiesOf('Form/ShakingButton', module)
  .add('Enable', () => {
    return {
      components,
      template:
        "<ShakingButton label='Green Icon Rectangular' icon='mail' color='green'/>"
    }
  })
  .add('Disable', () => {
    return {
      components,
      template: "<ShakingButton label='No icon round' round disable/>"
    }
  })

storiesOf('Form/ValidityIcon', module)
  .add('Valid', () => {
    return {
      components,
      template: '<ValidityIcon/>'
    }
  })
  .add('Not valid shown', () => {
    return {
      components,
      template: '<ValidityIcon knowError showError/>'
    }
  })
  .add('Not valid mandatory', () => {
    return {
      components,
      template: '<ValidityIcon knowError mandatory/>'
    }
  })

storiesOf('Form/InputWithValidation', module)
  .add('Valid edit icon', () => {
    return {
      components,
      template:
        "<InputWithValidation value='valid value' label='label' hint='hint' v-bind:knowError='false' id='validEditIcon'/>"
    }
  })
  .add('Error warning icon', () => {
    return {
      components,
      template:
        "<InputWithValidation value='invalid value' errorMessage='error message' showError knowError iconName='warning' id='errorWarningIcon'/>"
    }
  })

storiesOf('Form/CheckboxWithValidation', module)
  .add('Checked', () => {
    return {
      components,
      template: "<CheckboxWithValidation v-bind:value='true'/>"
    }
  })
