import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home'
import Blog from '@/views/Blog'
import Login from '@/views/Login'
import Github from '@/views/Github'
import ArticleDetail from '@/views/ArticleDetail'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  }, {
    path: '/post',
    name: 'post',
    component: Blog,
  }, {
    path: '/details/:slug',
    name: 'details',
    component: ArticleDetail,
    props: true,
  }, {
    path: '/login',
    name: 'login',
    component: Login,
  }, {
    path: '/github/auth',
    name: 'github',
    component: Github,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
