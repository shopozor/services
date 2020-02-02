import { storiesOf } from "@storybook/vue";
import TestComp from "./TestComponent.vue";

storiesOf("Tests", module).add("IconButtons", () => ({
  render: h => h(TestComp)
}));
