import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/components/Home"),
  },
  {
    path: "/post",
    name: "post",
    component: () => import("@/views/Blog"),
  },
  {
    path: "/details/:slug",
    name: "details",
    component: () => import("@/views/ArticleDetail"),
    props: true,
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/Login"),
  },
  {
    path: "/github/auth",
    name: "github",
    component: () => import("@/views/Github"),
  },
  {
    path: "/signup",
    name: "signup",
    component: () => import("@/views/Signup"),
  },
  {
    path: "/article/create",
    name: "create",
    component: () => import("@/views/CreateArticle"),
  },
  {
    path: "/article/update",
    name: "update",
    component: () => import("@/views/UpdateArticle"),
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
