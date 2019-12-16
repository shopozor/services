import { storiesOf } from '@storybook/vue'

storiesOf('First story', module)
  .add('Test', () => {
    return {
      template: '<h1>Petit test</h1>'
    }
  })
