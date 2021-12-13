<template>
  <div class="container text-xl p-4 flex flex-wrap space-between">
    <div
      v-for="(date, i) in archiveDates"
      :key="i"
      class="bg-blue-200 text-center align-middle p-2 
      md:mr-4 xs:mr-2 sm:mr-3 mb-3 cursor-pointer"
      @click="selectArchiveArticles(date)"
    >
      {{ date }}
    </div>
  </div>
  <div class="relative container mx-auto p-6 pt-1 flex flex-col space-y-6">
    <div
      class="absolute z-0 w-2 h-full bg-red-600
      border border-gray-300 shadow-md inset-0 left-17
      "
    ></div>
    <div
      class="h-16 w-16 rounded-full bg-purple-700
     border-2 border-blue-400 shadow-md ml-4 z-10 
     flex items-center justify-center"
    >
      {{ archiveYear }}
    </div>

    <div class="absolute left-32 flex justify-center align-center">
      <div
        class="p-4 xs:text-3xl sm:text-2xl lg:text-3xl text-red-500 inner-text"
      >
        天下事有难易乎？为之，则难者亦易矣；不为，则易者亦难矣。
      </div>
    </div>
    <div
      class="h-12 w-12 rounded-full bg-green-500
     border-2 border-blue-400 shadow-md ml-6 z-10
     flex items-center justify-center"
    >
      {{ archiveMonth }}
    </div>
    <div v-for="article in articles" :key="article.slug" class="relative z-10">
      <img
        class="h-24 w-24 object-cover 
        rounded-full shadow-md
        border-4 border-white xs:absolute 
        md:mx-auto"
        :src="getAvatar(article)"
        alt="头像"
      />
      <div class="relative pt-2 xs:pl-28 xs:pt-0">
        <div
          class="absolute inset-0 left-10 h-4 w-4 
        transform rotate-45 bg-gray-400 
        xs:top-11 xs:left-26"
          aria-hidden="true"
        ></div>
        <div class="bg-gray-400 p-6 rounded-md shadow-md">
          <span class="font-bold text-indigo-600 text-sm tracking-wide">
            {{ article.created_time }}
          </span>
          <router-link
            class="text-2xl font-bold pt-1"
            :to="{
              name: 'details',
              params: {
                slug: article.slug,
              },
            }"
            ><h1>{{ article.title }}</h1>
          </router-link>
          <p class="pt-1">
            {{ article.summery }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Cookies from "js-cookie";
import { reactive, toRefs, computed, onMounted } from "vue";
import { useStore } from "vuex";
export default {
  setup() {
    const state = reactive({
      archiveDates: [],
      isLoggedIn: computed(() => store.getters.isLoggedIn),
      articles: [],
      archiveYear: "",
      archiveMonth: "",
    });
    const store = useStore();
    const selectArchiveArticles = (date) => {
      // console.log(date);
      state.archiveYear = date.split("-")[0];
      state.archiveMonth = date.split("-")[1];
      const url = `api/blog/archive/${state.archiveYear}/${state.archiveMonth}`;
      axios
        .get(url, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          state.articles = res.data;
        })
        .catch((e) => console.log(e));
    };
    const getArchiveArticles = (url = "/api/blog/archive/dates") => {
      axios
        .get(url, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          state.archiveDates.push(
            ...res.data.map((v) => v.split("-")[0] + "-" + v.split("-")[1])
          );
          if (state.archiveDates.length > 0) {
            selectArchiveArticles(state.archiveDates[0]);
          }
          // console.log(state);
        })
        .catch((e) => console.log(e));
    };
    const getAvatar = (article) => {
      if (article.author.user !== null) {
        return article.author.user.avatar_url;
      } else if (article.author.avatar !== null) {
        return article.author.avatar.content;
      } else {
        return "https://img.paulzzh.com/touhou/random";
      }
    };
    onMounted(() => {
      getArchiveArticles();
    });
    return {
      ...toRefs(state),
      getArchiveArticles,
      selectArchiveArticles,
      store,
      getAvatar,
    };
  },
};
</script>
<style>
@media only screen and (min-width: 768px) {
  .inner-text {
    overflow: hidden;
    position: relative;
    width: 100%;
    border-right: 2px solid rgba(255, 255, 255, 0.75);
    white-space: nowrap;
    /*
    animation-name: typewriter;
    animation-duration: 4s;
    animation-timing-function: steps(44);
    animation-delay: 1s;
    animation-iteration-count: 1;
    animation-direction: normal;
    animation-fill-mode: both;
    */
    animation: typewriter 4s steps(44) 1s 1 normal both,
      blinkTextCursor 600ms steps(44) infinite normal;
  }
  @keyframes typewriter {
    from {
      width: 0;
    }

    to {
      width: 100%;
    }
  }

  @keyframes blinkTextCursor {
    from {
      border-right-color: rgba(187, 35, 35, 0.75);
    }

    to {
      border-right-color: transparent;
    }
  }
}
</style>
