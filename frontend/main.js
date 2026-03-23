// This is the main entry point for the Vue.js application.
import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'
import './index.css'

createApp(App).use(router).mount('#app')
