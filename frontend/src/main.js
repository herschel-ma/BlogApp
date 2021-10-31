import { createApp } from 'vue'
import router from './routers'
import App from './App.vue'
import '@/assets/tailwind.css'
import store from './store'

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')
