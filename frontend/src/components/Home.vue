<template>
  <!-- component -->
  <div class="flex flex-wrap">
    <!-- post section -->
    <section class="w-full md:w-2/3 flex flex-col items-center px-3 mt-6">
      <div class="w-full lg:w-8/12">
        <div class="flex items-center justify-between">
          <h1 class="text-xl font-bold text-gray-700 md:text-2xl">博文</h1>
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
                  {{ article.category.title }}
                </router-link>
              </div>
              <div class="mt-2">
                <a
                  href="#"
                  class="text-2xl font-bold text-gray-700 hover:underline"
                  >{{ article.title }}</a
                >
                <p
                  v-if="article.content"
                  v-html="article.content"
                  class="mt-2 text-gray-600"
                ></p>
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
                      stroke="indigo"
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
                      stroke="red"
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
                    <h1
                      class="font-bold text-gray-700 sm:text-sm md:text-xl hover:underline"
                    >
                      {{ article.author.username }}
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
        <!-- paganation -->
        <!-- <page-nation :results="counted" @clickPagenation="handleClickPagenation" /> -->
        <transition
          appear
          enter-active-class="transition delay-500 duration-1000 ease-out"
          enter-from-class="opacity-0 transform translate-x-24"
          enter-to-class="opacity-100"
        >
          <div class="mt-8">
            <v-pagination
              v-model="page"
              :pages="totalPages"
              :range-size="1"
              active-color="#DCEDFF"
              @update:modelValue="updateHandler"
            />
          </div>
        </transition>
      </div>
    </section>
    <aside class="mt-6 md:w-1/3 w-full hidden md:block lg:block lg:-mx-10">
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
        <recent-post />
      </transition>
      <div class="lg:-ml-14 md:-ml-36 sm:hidden md:hidden lg:block">
        <Tags :width="width" :height="height" :RADIUS="radius" />
      </div>
    </aside>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import axios from "axios";
import { onMounted, toRefs, reactive, computed } from "vue";
import Authors from "@/components/Authors";
import Category from "@/components/Category";
import RecentPost from "@/components/RecentPost";
import VPagination from "@hennge/vue3-pagination";
import Tags from "@/views/Tags";
import "@hennge/vue3-pagination/dist/vue3-pagination.css";
import { useToast } from "vue-toastification";
import { useStore } from "vuex";

export default {
  components: {
    Authors,
    Category,
    RecentPost,
    VPagination,
    Tags,
  },
  setup() {
    const toast = useToast();
    const store = useStore();
    const state = reactive({
      articles: [],
      results: {},
      totalPages: 0,
      args: "yyy-mm-dd hh:mm:ss",
      page: 1,
      width: 500,
      height: 500,
      radius: 200,
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
    const getAllArticles = (url = "/api/blog/") => {
      axios
        .get(url, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((response) => {
          state.results = response.data;
          state.totalPages = response.data.total_pages;
          return response.data.results;
        })
        .then((results) => {
          state.articles = [];
          state.articles.push(
            ...results.map((a) => {
              const options = {
                weekday: "long",
                year: "numeric",
                month: "long",
                day: "numeric",
                hour: "numeric",
                minute: "2-digit",
                second: "2-digit",
                hour12: false,
              };
              a.created_time = new Date(a.created_time).toLocaleDateString(
                // "en-US",
                "zh-hans",
                options
              );
              a.content = a.summery;
              return a;
            })
          );
        })
        .catch((error) => console.log(error));
    };
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
    const updateHandler = (number) => {
      let url = `/api/blog?page=${number}`;
      if (url === "/api/blog?page=1") {
        url = "/api/blog/";
      }
      getAllArticles(url);
    };
    const askMediaScreen = () => {
      // var result = window.matchMedia("(max-width:418px)"); //要加括号
      var result2 = window.matchMedia("(max-width:768px)");
      var result3 = window.matchMedia("(max-width:992px)");
      if (result2.matches) {
        state.width = 100;
        state.height = 100;
        state.radius = 25;
      } else if (result3.matches) {
        state.width = 400;
        state.height = 400;
        state.radius = 25;
      }
    };
    onMounted(() => {
      getAllArticles();
      askMediaScreen();
    });
    return {
      toast,
      store,
      ...toRefs(state),
      getAllArticles,
      handleDelete,
      updateHandler,
      askMediaScreen,
      randomColor,
    };
  },
};
</script>
