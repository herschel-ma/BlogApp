import { createApp } from "vue";
import router from "./routers";
import App from "./App.vue";
import "@/assets/tailwind.css";
import store from "./store";
// markdown editor

// Toast
import Toast from "vue-toastification";

// Import the CSS or use your own!
import "vue-toastification/dist/index.css";

import './assets/tailwind.css'
const options = {};

const app = createApp(App);
app.use(store);
app.use(router);
app.use(Toast, options);
app.mount("#app");
