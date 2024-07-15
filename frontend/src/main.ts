import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import all_components from '@/components/index'


const app = createApp(App)
all_components.forEach(component => {
    app.component(component.name, component)
})

app
    .use(store)
    .use(router)
    .mount('#app')
