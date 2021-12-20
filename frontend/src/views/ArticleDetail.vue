<template>
  <div class="w-full" :class="{ is_fixed: isProcessFixed }">
    <div
      id="processBar"
      class="overflow-hidden h-1 text-xs flex rounded bg-purple-200"
    >
      <div
        :style="{ width: progressWidth }"
        class="
        shadow-none
        flex flex-col
        text-center
        whitespace-nowrap
        text-white
        justify-center
        bg-purple-500
      "
      ></div>
    </div>
    <div class="flex items-center justify-between">
      <div class="text-right">
        <span class="text-xs font-semibold inline-block text-purple-600">
          {{ progressWidth }}
        </span>
      </div>
    </div>
  </div>
  <div class="container mx-auto flex flex-wrap">
    <!-- Post Section -->
    <section class="w-full md:w-2/3 flex flex-col xxs:px-0 md:px-3 ">
      <article class="flex flex-col shadow my-4">
        <!-- Article Image -->
        <a class="hover:opacity-75">
          <img
            :src="
              musicPicurl
                ? musicPicurl
                : 'https://img.paulzzh.com/touhou/random'
            "
          />
        </a>
        <div class="bg-white flex flex-col justify-center p-6">
          <a
            v-if="article.category"
            class="text-blue-700 text-sm font-bold uppercase pb-4"
          >
            <span
              class="text-sm font-semibold inline-block
              py-1 px-2 uppercase rounded-full
              text-purple-600 bg-purple-200"
            >
              {{ article.category.title }}
            </span>
          </a>
          <a class="text-3xl font-bold hover:text-gray-700 pb-4"
            >{{ article.title }}

            <div
              class="
                  relative
                  inline-block
                  w-10
                  mr-2
                  align-middle
                  select-none
                  transition
                  duration-200
                  ease-in
                "
            >
              <input
                type="checkbox"
                name="toggle"
                id="toggle"
                @change="handleChanged($event)"
                class="
                  toggle-checkbox
                  absolute
                  block
                  w-6
                  h-6
                  rounded-full
                  bg-white
                  border-4
                  appearance-none
                  cursor-pointer
                  "
              />
              <label
                for="toggle"
                class="
                  toggle-label
                  block
                  overflow-hidden
                  h-6
                  rounded-full
                  bg-gray-300
                  cursor-pointer
                  "
              ></label>
            </div>
            <label for="toggle" class="text-xs text-gray-700"
              >切换预览主题</label
            >
          </a>
          <div
            v-if="musicUrl"
            class="flex xs:flex-row items-center md:justify-between lg:justify-start mb-3 px-1 pt-2"
          >
            <div
              class="flex flex-col space-y-1 max-w-max whitespace-nowrap mr-2"
            >
              <div class="text-xs m-0 p-0">{{ musicName }}</div>
              <div class="text-xs m-0 p-0">{{ musicArtistsname }}</div>
            </div>
            <audio :src="musicUrl" controls>
              您的浏览器不支持播放音乐...
            </audio>
          </div>
          <p class="text-sm pb-8">
            作者：
            <a class="font-semibold hover:text-gray-800">{{
              article.author ? article.author.username : ""
            }}</a>
            , 发布于 {{ article.created_time }}
          </p>
          <div class="md-e">
            <md-editor
              v-model="article.content"
              :preview-theme="theme"
              :previewOnly="true"
              @onGetCatalog="onGetCatalog"
            />
          </div>
        </div>
        <div
          v-show="show"
          @click="clickTopHandle"
          class="fixed right-20 bottom-20
      w-8 h-8 md:h-16 md:w-16 rounded-full 
      flex justify-center items-center  
      bg-blue-400 opacity-60 
      hover:bg-gray-400 transition duration-100"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 md:h-10 md:w-10"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"
            />
          </svg>
        </div>
        <a
          href="#comment-form"
          v-show="show"
          class="fixed md:right-36 right-28 bottom-20
      w-8 h-8 md:h-16 md:w-16 rounded-full 
      flex justify-center items-center  
      bg-indigo-400 opacity-60 
      hover:bg-gray-400 transition duration-100"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 md:h-10 md:w-10"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M18 10c0 3.866-3.582 7-8 7a8.841 8.841 0 01-4.083-.98L2 17l1.338-3.123C2.493 12.767 2 11.434 2 10c0-3.866 3.582-7 8-7s8 3.134 8 7zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z"
              clip-rule="evenodd"
            />
          </svg>
        </a>
      </article>

      <div class="w-full flex pt-6">
        <a class="w-1/2 bg-white shadow hover:shadow-md text-left p-6">
          <p
            class="text-blue-800 hover:underline text-lg font-bold flex items-center cursor-pointer"
            @click="toPrev"
          >
            上一篇
          </p>
          <a class="pt-2">{{ messagePrev }}</a>
        </a>
        <a
          class="w-1/2 items-end flex flex-col text-justify bg-white shadow hover:shadow-md p-6"
        >
          <p
            class="text-blue-800 hover:underline text-lg font-bold flex items-center cursor-pointer"
            @click="toNext"
          >
            下一篇
          </p>
          <a class="pt-2">{{ messageNext }}</a>
        </a>
      </div>

      <!-- comments here -->
      <Comments :article="article" />
      <div
        v-if="article.author && article.author.description"
        class="w-full flex flex-col text-center md:text-left md:flex-row shadow bg-white mt-10 mb-10 p-6 pb-3"
      >
        <div class="w-full md:w-1/5 flex justify-center md:justify-start pb-4">
          <img
            :src="getAvatar(article)"
            class="rounded-full object-cover shadow h-32 w-32"
          />
        </div>
        <div
          class="flex-1 flex flex-col justify-center md:justify-start md:pl-10"
        >
          <p class="font-semibold text-2xl">{{ article.author.username }}</p>
          <p class="pt-2">
            {{ article.author.description }}
          </p>
        </div>
      </div>
    </section>

    <!-- Sidebar Section -->
    <aside class="w-full md:w-1/3 flex flex-col px-3">
      <div
        v-if="articles.length > 0"
        class="w-full bg-white shadow flex flex-col my-4 p-6 space-y-3 justify-center align-middle"
      >
        <h1 class="mb-4 text-xl font-bold text-gray-700">相似文章</h1>
        <div
          v-for="a in articles"
          :key="a.id"
          class="flex flex-col px-8 py-6 bg-white rounded-lg shadow-md justify-center align-middle"
        >
          <div class="flex items-center justify-center">
            <a
              v-if="a.category"
              class="px-2 py-1 text-sm text-green-100 bg-gray-600 rounded hover:bg-gray-500"
              >{{ a.category.title }}</a
            >
          </div>
          <router-link
            class="mt-4 text-center"
            :to="{
              name: 'details',
              params: {
                slug: a.slug,
              },
            }"
          >
            {{ a.title }}
          </router-link>
          <div
            class="flex space-y-3 items-center justify-center
            md:flex-col md:justify-center md:space-x-0 md:space-y-3  
            lg:flex-row lg:space-y-0 lg:justify-between lg:space-x-12 
            sm:flex-row sm:space-y-0 sm:justify-between sm:space-x-12
            xs:flex-row sm:space-y-0 xs:justify-between sm:space-x-12 xxs:space-y-0"
          >
            <div class="flex items-center align-center md:mt-2 lg:mt-0">
              <img
                :src="getAvatar(a)"
                alt="avatar"
                class="object-cover w-8 h-8 rounded-full"
              />
              <a class="mx-3 text-sm text-gray-700 hover:underline">{{
                a.author.username
              }}</a>
            </div>
            <span class="text-sm font-light text-gray-600">{{
              a.created_time
            }}</span>
          </div>
        </div>
      </div>
      <div id="photo" class="w-full bg-white shadow flex flex-col my-4 p-6">
        <p class="text-xl font-bold text-gray-700 pb-5">图片集</p>
        <div class="grid grid-cols-3 gap-3">
          <img
            v-for="i in 9"
            :key="i"
            class="hover:opacity-75"
            src="https://img.paulzzh.com/touhou/random"
          />
        </div>
        <a
          class="w-full bg-blue-800 text-white font-bold text-sm uppercase rounded hover:bg-blue-700 flex items-center justify-center px-2 py-3 mt-6"
        >
          <i class="fab fa-instagram"></i> Follow @dgrzyb
        </a>
        <div id="boxFixed" ref="box"></div>
      </div>
      <div
        v-if="catalogList.length > 0"
        class="bg-white mt-4 p-2 xxs:hidden 
        sm:hidden md:block lg:block
        shadow boxFiexd"
        :class="{ is_fixed: isFixed }"
      >
        <button
          class="w-16 h-8 rounded-md bg-pink-200 
        hover:bg-red-600 transition duration-500 mb-2"
        >
          目录
        </button>
        <div
          v-for="(catalog, i) in catalogList"
          :key="i"
          class="hover:bg-gray-300 transition duration-500"
        >
          <a :href="`#${catalog.text}`" :class="`catalog-${catalog.level}`">{{
            catalog.text
          }}</a>
        </div>
      </div>
    </aside>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import axios from "axios";
import {
  reactive,
  toRefs,
  computed,
  onMounted,
  nextTick,
  onUnmounted,
  ref,
} from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import MdEditor from "md-editor-v3";
import "md-editor-v3/lib/style.css";
import Comments from "@/components/Comments";
export default {
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  components: { MdEditor, Comments },
  watch: {
    // 监听路由变化获取上一章|下一章内容
    $route(to) {
      if (to.fullPath.startsWith("/details")) {
        this.getArticle(to.params.slug);
        this.getPrevNext(to.params.slug);
      }
    },
  },
  setup(props) {
    const store = useStore();
    const router = useRouter();
    let box = ref(null);
    const state = reactive({
      article: {},
      articles: [],
      theme: "default",
      messagePrev: null,
      messageNext: null,
      prevSlug: "",
      nextSlug: "",
      catalogList: [],
      catalogHtmlTitle: [],
      isFixed: false,
      isProcessFixed: false,
      progressWidth: null,
      offsetTop: 0,
      offsetHeight: 0,
      offsetProcessBarTop: 0,
      scrollTop: 0,
      isLoggedIn: computed(() => store.getters.isLoggedIn),
      show: false,
      musicName: "",
      musicUrl: "",
      musicPicurl: "",
      musicArtistsname: "",
    });
    const getArticle = (slug = props.slug) => {
      axios
        .get(`/api/blog/${slug}/`, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          state.article = res.data;
        })
        .catch((error) => console.log(error));
    };
    const getPrevNext = (slug = props.slug) => {
      axios
        .get(`/api/blog/${slug}?prev`, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          state.messagePrev = res.data.message || res.data.title;
          state.prevSlug = res.data.slug || props.slug;
        })
        .catch((e) => {
          console.log(e.response.message);
        });
      axios
        .get(`/api/blog/${slug}?next`, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          state.messageNext = res.data.message || res.data.title;
          state.nextSlug = res.data.slug || props.slug;
        })
        .catch((e) => console.log(e));
      axios
        .get(`/api/blog/${slug}?similar`, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((response) => {
          return response.data;
        })
        .then((results) => {
          state.articles = [];
          state.articles.push(
            ...results.map((a) => {
              a.created_time = new Date(a.created_time).toLocaleDateString(
                "zh-hans"
              );
              return a;
            })
          );
        })
        .catch((e) => console.log(e));
    };
    const onGetCatalog = (list) => {
      state.catalogList = [];
      state.catalogList.push(
        ...list.map((cat) => {
          return cat;
        })
      );
    };
    const initHeight = () => {
      // 设置或获取位于对象最顶端和窗口中可见内容的最顶端之间的距离 (被卷曲的高度)
      var scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      //如果被卷曲的高度大于吸顶元素到顶端位置 的距离
      let offset = 0;
      if (state.articles.length > 0) {
        if (state.articles.length == 1) {
          offset = 406;
        } else if (state.articles.length == 2) {
          offset = 506;
        } else if (state.articles.length == 3) {
          offset = 706;
        }
      }
      // 页面总高度
      let pageHeight =
        document.documentElement.scrollHeight || document.body.scrollHeight;
      // 浏览器视口高度
      let windowHeight =
        document.documentElement.clientHeight || document.body.clientHeight;
      // 可滚动的高度
      let scrollAvail = pageHeight - windowHeight;
      // 滚动占比值取两位
      let scrollPercent = Number(
        (scrollTop / scrollAvail).toString().match(/^\d+(?:\.\d{0,2})?/)
      );
      state.progressWidth = scrollPercent * 100 + "%";
      // catalog
      state.isFixed = scrollTop > state.offsetTop + offset ? true : false;
      // progress bar
      state.isProcessFixed =
        scrollTop > state.offsetProcessBarTop ? true : false;
      // top function
      const winHeight = document.documentElement.clientHeight;
      let scrollHeight = document.documentElement.scrollTop;
      state.show = winHeight < scrollHeight ? true : false;
    };
    const getMusicInfo = () => {
      const url = "https://api.uomg.com/api/rand.music?sort=热歌榜&format=json";
      axios
        .get(url)
        .then((res) => {
          if (res.data.code === 1) {
            state.musicName = res.data.data.name;
            state.musicUrl = res.data.data.url;
            state.musicPicurl = res.data.data.picurl;
            state.musicArtistsname = res.data.data.artistsname;
          }
        })
        .catch((e) => {
          console.error(e);
        });
    };

    onMounted(() => {
      window.addEventListener("scroll", initHeight);
      nextTick(() => {
        //获取对象相对于版面或由 offsetTop 属性指定的父坐标的计算顶端位置
        state.offsetTop = document.querySelector("#boxFixed").offsetTop;
        state.offsetProcessBarTop = document.querySelector(
          "#processBar"
        ).offsetTop;
      });
      getMusicInfo();
    });
    onUnmounted(() => {
      window.removeEventListener("scroll", initHeight);
    });
    const clickTopHandle = () => {
      document.documentElement.scrollTop = 0;
    };
    const handleChanged = () => {
      if (state.theme === "default") {
        state.theme = "github";
      } else if (state.theme === "vuepress") {
        state.theme = "github";
      } else if (state.theme === "github") {
        state.theme = "vuepress";
      }
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
    getArticle();
    getPrevNext();

    return {
      ...toRefs(state),
      router,
      getArticle,
      getPrevNext,
      onGetCatalog,
      toPrev: () => {
        router.replace({
          name: "details",
          params: { slug: state.prevSlug },
        });
      },
      toNext: () => {
        router.replace({
          name: "details",
          params: { slug: state.nextSlug },
        });
      },
      initHeight,
      clickTopHandle,
      handleChanged,
      getAvatar,
      box,
    };
  },
};
</script>

<style scope>
.is_fixed {
  position: fixed;
  top: 0;
  z-index: 999;
}
.md-e {
  /*父元素设置为flex后，子元素会自动布局并适应宽度，
  但里面的文本文字超出边界却无法换 */
  overflow-wrap: break-word;
}
h1 {
  font-size: 30px;
}
h2 {
  font-size: 28px;
}
h3 {
  font-size: 22px;
}
h4 {
  font-size: 18px;
}
h5 {
  font-size: 14px;
}
h6 {
  font-size: 10px;
}
.catalog-1 {
  color: rgb(97, 168, 173);
}
.catalog-2 {
  margin-left: 1em;
  color: rgb(97, 168, 173);
}
.catalog-3 {
  margin-left: 2em;
  font-size: 16px;
  color: rgb(111, 116, 161);
}
.catalog-4 {
  margin-left: 3em;
  font-size: 14px;
  color: rgb(111, 116, 161);
}
.catalog-5 {
  margin-left: 4em;
  font-size: 14px;
  color: rgb(153, 119, 185);
}
.catalog-6 {
  margin-left: 5em;
  font-size: 14px;
  color: rgb(153, 119, 185);
}
/* CHECKBOX TOGGLE SWITCH */
/* @apply rules for documentation, these do not work as inline style */
.toggle-checkbox:checked {
  right: 0;
  border-color: #68d391;
}
.toggle-checkbox:checked + .toggle-label {
  background-color: #68d391;
}
</style>
