<template>
  <div class="px-8 mt-10 flex flex-col space-y-3">
    <h1 class="mb-4 text-xl font-bold text-gray-700">最近发布</h1>
    <div
      v-for="article in articles"
      :key="article.id"
      class="flex flex-col max-w-sm px-8 py-6 bg-white rounded-lg shadow-md"
    >
      <div class="flex items-center justify-center">
        <a
          href="#"
          class="px-2 py-1 text-sm text-green-100 bg-gray-600 rounded hover:bg-gray-500"
          >{{ article.category.title }}</a
        >
      </div>
      <router-link
        class="mt-4 text-center"
        :to="{
          name: 'details',
          params: {
            slug: article.slug,
          },
        }"
      >
        {{ article.title }}
      </router-link>
      <div
        class="flex flex-col space-y-3 items-center  lg:flex-row lg:space-y-0 lg:justify-between"
      >
        <div class="flex items-center align-center md:mt-2 lg:mt-0">
          <img
            src="https://img.paulzzh.com/touhou/random"
            alt="avatar"
            class="object-cover w-8 h-8 rounded-full"
          />
          <a href="#" class="mx-3 text-sm text-gray-700 hover:underline">{{
            article.author
          }}</a>
        </div>
        <span class="text-sm font-light text-gray-600">{{
          article.last_updated_time
        }}</span>
      </div>
    </div>
  </div>
</template>
<script>
import Cookies from "js-cookie";
import axios from "axios";
import { onMounted, toRefs, reactive, computed } from "vue";
import { useStore } from "vuex";

export default {
  setup() {
    const store = useStore();
    const state = reactive({
      articles: [],
      results: {},
      args: "yyy-mm-dd hh:mm:ss",
      page: 1,
      isLoggedIn: computed(() => store.getters.isLoggedIn),
    });
    const getAllArticles = (url = "/api/blog_recent") => {
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
          return response.data;
        })
        .then((results) => {
          state.articles = [];
          state.articles.push(
            ...results.map((a) => {
              a.last_updated_time = new Date(
                a.last_updated_time
              ).toLocaleDateString("zh-hans");
              return a;
            })
          );
        })
        .catch((error) => console.log(error));
    };

    onMounted(() => {
      getAllArticles();
    });
    return {
      store,
      ...toRefs(state),
      getAllArticles,
    };
  },
};
</script>
