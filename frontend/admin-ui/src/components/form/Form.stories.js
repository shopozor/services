import { storiesOf } from "@storybook/vue";
import ShakingButton from "./ShakingBtn.vue";

const components = { ShakingButton };

storiesOf("Form", module)
  .add("ShakingButton_Enable", () => {
    return {
      components,
      template:
        "<ShakingButton label='Green Icon Rectangular' icon='mail' color = 'green'/>"
    };
  })
  .add("ShakingButton_Disable", () => {
    return {
      components,
      template: "<ShakingButton label='No Icon round' round disable/>"
    };
  });
