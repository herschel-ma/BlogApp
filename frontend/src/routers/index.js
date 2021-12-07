import { createRouter, createWebHistory } from "vue-router";
import { useToast } from "vue-toastification";
import store from "@/store";
const toast = useToast();
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
  {
    path: "/category",
    name: "category",
    component: () => import("@/views/CategoryDetail"),
    props: true,
  },
  {
    path: "/archive",
    name: "archive",
    component: () => import("@/views/ArchiveBlog"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.name !== "login" && to.name !== "github" && !store.state.isLoggedIn) {
    next({ name: "login" });
  }
  if (
    to.name === "update" &&
    store.state.isLoggedIn &&
    to.params.author &&
    to.params.author !== localStorage.getItem("user_name")
  ) {
    next(false);
    toast.error(
      `${localStorage.getItem("user_name")}, 您没有权限修改${
        to.params.author
      }的文章!`,
      {
        timeout: 2500,
      }
    );
  } else {
    next();
  }
});
export default router;
