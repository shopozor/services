import { storiesOf } from '@storybook/vue'
import VueI18n from 'vue-i18n'
import LanguageSelect from './LanguageSelect'

const components = {
  LanguageSelect
}

storiesOf('I18n/LanguageSelect', module)
  .add('Disable', () => ({
    components,
    template: '<div style="background-color:lightblue"> <LanguageSelect /> </div>',
    i18n: new VueI18n({ locale: 'fr' })
  })
  )
