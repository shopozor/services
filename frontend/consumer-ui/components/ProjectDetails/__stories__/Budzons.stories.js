import { storiesOf } from '@storybook/vue'
import Budzons from '../Budzons'
import ProjectOverview from '../ProjectOverview'

storiesOf('Budzons', module)
  .add('Budzons', () => {
    return {
      components: {
        Budzons
      },
      template: '<budzons />'
    }
  })
  .add('Project overview', () => {
    return {
      components: {
        ProjectOverview
      },
      template: '<project-overview />'
    }
  })
