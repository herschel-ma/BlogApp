<template>
  <!-- component -->
  <div class="bg-gray-100 flex flex-wrap">
    <!-- post section -->
    <section class="w-full md:w-2/3 flex flex-col items-center px-3 mt-6">
      <div class="w-full lg:w-8/12">
        <div class="flex items-center justify-between">
          <h1 class="text-xl font-bold text-gray-700 md:text-2xl">
            {{ route.query.tag }}
          </h1>
          <div>
            <select
              class="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            >
              <option>Latest</option>
              <option>Last Week</option>
            </select>
          </div>
        </div>
        <div class="mt-6" v-for="article in articles" :key="article.id">
          <transition
            appear
            enter-active-class="transition delay-500 duration-1000 ease-out"
            enter-from-class="opacity-0 transform translate-y-24"
            enter-to-class="opacity-100"
          >
            <div
              class="max-w-4xl px-10 py-6 mx-auto bg-white rounded-lg shadow-md"
            >
              <div class="flex items-center justify-between">
                <span class="font-light text-gray-600">{{
                  article.created_time
                }}</span>
                <router-link
                  v-if="article.category"
                  :to="{
                    name: 'category',
                    query: {
                      cate: article.category.title,
                      id: article.category.id,
                    },
                  }"
                  class="px-2 py-1 font-bold text-gray-100 bg-gray-600 rounded hover:bg-gray-500"
                >
                  {{ article.category.title }}</router-link
                >
              </div>
              <div class="mt-2">
                <a class="text-2xl font-bold text-gray-700 hover:underline">{{
                  article.title
                }}</a>
                <p class="mt-2 text-gray-600">{{ article.summery }}</p>
              </div>
              <div class="flex items-center justify-between mt-4">
                <div class="flex space-x-2">
                  <router-link
                    class="text-blue-500 hover:underline"
                    :to="{
                      name: 'details',
                      params: {
                        slug: article.slug,
                      },
                    }"
                    >【阅读全文】
                  </router-link>
                  <router-link
                    :to="{
                      name: 'update',
                      params: {
                        slug: article.slug,
                        author: article.author.username,
                      },
                    }"
                  >
                    <svg
                      class="w-6 h-6 text-gray-600 hover:text-blue-500"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
                      />
                    </svg>
                  </router-link>
                  <a href @click="handleDelete($event, article.slug)">
                    <svg
                      class="w-6 h-6 text-gray-600 hover:text-blue-500"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                      />
                    </svg>
                  </a>
                </div>
                <div>
                  <a class="flex items-center">
                    <img
                      v-if="article.author.user"
                      :src="article.author.user.avatar_url"
                      alt="avatar"
                      class="hidden object-cover w-10 h-10 mx-4 rounded-full sm:block"
                    />
                    <img
                      v-else
                      src="https://img.paulzzh.com/touhou/random"
                      alt="avatar"
                      class="hidden object-cover w-10 h-10 mx-4 rounded-full sm:block"
                    />
                    <h1 class="font-bold text-gray-700 hover:underline">
                      {{ article.author }}
                    </h1>
                  </a>
                </div>
              </div>
              <div v-if="article.tags" class="flex space-x-3">
                <button
                  v-for="(tag, i) in article.tags"
                  :key="i"
                  ref="button"
                  class="py-1 px-2 rounded-lg shadow-lg mt-2 flex justify-center align-middle"
                  :class="randomColor(i)"
                >
                  <router-link
                    :to="{
                      name: 'tags',
                      query: {
                        tag: tag,
                      },
                    }"
                    >{{ tag }}
                  </router-link>
                </button>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </section>
    <aside class="mt-6 md:w-1/3 w-full hidden lg:block -mx-10">
      <!--Authors-->
      <transition
        appear
        enter-active-class="transition delay-3000 duration-1000 ease-out"
        enter-from-class="opacity-0 transform translate-y-2"
        enter-to-class="opacity-100"
      >
        <Authors />
      </transition>

      <transition
        appear
        enter-active-class="transition delay-2000 duration-1000 ease-out"
        enter-from-class="opacity-0 transform translate-y-11"
        enter-to-class="opacity-100"
      >
        <Category />
      </transition>

      <transition
        appear
        enter-active-class="transition delay-500 duration-1000 ease-out"
        enter-from-class="opacity-0 transform translate-y-20"
        enter-to-class="opacity-100"
      >
      </transition>
    </aside>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import axios from "axios";
import { toRefs, reactive, computed } from "vue";
import Authors from "@/components/Authors";
import Category from "@/components/Category";
import "@hennge/vue3-pagination/dist/vue3-pagination.css";
import { useToast } from "vue-toastification";
import { useStore } from "vuex";
import { useRoute } from "vue-router";

export default {
  components: {
    Authors,
    Category,
  },
  watch: {
    // 监听路由变化获取标签文章
    $route(to) {
      if (to.fullPath.startsWith("/tags")) {
        this.getArticles("", to.query);
      }
    },
  },
  setup() {
    const toast = useToast();
    const store = useStore();
    const route = useRoute();
    const state = reactive({
      articles: [],
      results: {},
      isLoggedIn: computed(() => store.getters.isLoggedIn),
    });
    const randomColor = (i) => {
      const colors = [
        "red",
        "gray",
        "blue",
        "indigo",
        "pink",
        "purple",
        "yellow",
        "orange",
      ];
      const text = [
        "100",
        "200",
        "300",
        "400",
        "500",
        "600",
        "700",
        "800",
        "900",
      ];
      if (i > colors.length) {
        i = 0;
      } else if (i > text.length) {
        i = 0;
      }
      return `bg-${colors[i]}-${text[i]}`;
    };
    const getArticles = (url = "", query = route.query) => {
      state.articles = [];
      if (url == "") {
        url = `/api/blog/archive/tags/?tag_name=${query.tag}`;
      }
      axios.get(url).then((res) => {
        state.articles.push(...res.data);
      });
    };
    getArticles();
    const handleDelete = (event, slug) => {
      event.preventDefault();
      axios
        .delete(`/api/blog/${slug}/`, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          if (res.stauts === "204" || res.status === 204) {
            toast.success(`删除${slug}成功`, {
              timeout: 2000,
            });
            setTimeout(() => {
              window.location.href = "/";
            }, 1000);
          }
        })

        .catch((e) => {
          if (e.response) {
            if (e.response.data.detail) {
              toast.error(e.response.data.detail, {
                timeout: 2000,
              });
            } else {
              toast.error(`删除${slug}失败，请重试`, {
                timeout: 2000,
              });
            }
          }
        });
    };

    return {
      toast,
      store,
      route,
      ...toRefs(state),
      handleDelete,
      getArticles,
      randomColor,
    };
  },
};
</script>
