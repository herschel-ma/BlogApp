import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home'
import Blog from './views/Blog'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/post',
    name: 'post',
    component: Blog,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
