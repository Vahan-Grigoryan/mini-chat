import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Welcome from '@/views/Welcome.vue'
import Registration from '@/views/Registration.vue'
import Login from '@/views/Login.vue'
import Home from '@/views/Home.vue'


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'index',
    component: Welcome
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/registration',
    name: 'registration',
    component: Registration
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
