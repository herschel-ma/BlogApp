import { createApp } from 'vue'
import router from './routers'
import App from './App.vue'
import '@/assets/tailwind.css'

const app = createApp(App)
app.use(router)
app.mount('#app')
