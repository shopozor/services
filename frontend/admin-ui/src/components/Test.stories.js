import { storiesOf } from "@storybook/vue";
import TestComp from "./TestComponent.vue";

storiesOf("Buttons", module).add("MyButton", () => ({
  render: h => h(TestComp)
}));
