import { storiesOf } from "@storybook/vue";
import ShakingButton from "./ShakingBtn.vue";
import ValidityIcon from "./ValidityIcon.vue";
import InputWithValidation from "./InputWithValidation.vue";
import CheckboxWithValidation from "./CheckboxWithValidation.vue";

const components = {
  ShakingButton,
  ValidityIcon,
  InputWithValidation,
  CheckboxWithValidation
};

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

storiesOf("Form", module)
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

storiesOf("Form", module)
  .add("InputWithValidation_Valid_EditIcon", () => {
    return {
      components,
      template:
        "<InputWithValidation value='valid value' label='label' hint='hint' v-bind:knowError='false'/>"
    };
  })
  .add("InputWithValidation_Error_WarningIcon", () => {
    return {
      components,
      template:
        "<InputWithValidation value='unvalid value' errorMessage='error message' showError knowError iconName='warning'/>"
    };
  });

storiesOf("Form", module).add("CheckboxWithValidation_checked", () => {
  return {
    components,
    template: "<CheckboxWithValidation v-bind:value='true'/>"
  };
});
