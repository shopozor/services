import { storiesOf } from "@storybook/vue";
import ShakingButton from "./ShakingBtn.vue";
import ValidityIcon from "./ValidityIcon.vue";

const components = { ShakingButton, ValidityIcon };

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
  })
  .add("ValidityIcon_Valid", () => {
    return {
      components,
      template: "<ValidityIcon/>"
    };
  })
  .add("ValidityIcon_NotValidShown", () => {
    return {
      components,
      template: "<ValidityIcon knowError showError/>"
    };
  })
  .add("ValidityIcon_NotValidMandatory", () => {
    return {
      components,
      template: "<ValidityIcon knowError mandatory/>"
    };
  });
