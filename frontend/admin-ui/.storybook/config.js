import { configure } from "@storybook/vue";

import Vue from "vue";
import Quasar from "quasar";

import "quasar/dist/quasar.sass";
import "@quasar/extras/material-icons/material-icons.css";
import "@quasar/extras/roboto-font/roboto-font.css";
//animations
import "@quasar/extras/animate/shake.css";

Vue.use(Quasar);

// automatically import all files ending in *.stories.js
configure(require.context("../src", true, /\.stories\.js$/), module);
