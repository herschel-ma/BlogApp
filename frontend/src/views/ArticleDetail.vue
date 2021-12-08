<template>
  <div class="container mx-auto flex flex-wrap py-6">
    <!-- Post Section -->
    <section class="w-full md:w-2/3 flex flex-col px-3 ">
      <article class="flex flex-col shadow my-4">
        <!-- Article Image -->
        <a class="hover:opacity-75">
          <img src="https://img.paulzzh.com/touhou/random" />
        </a>
        <div class="bg-white flex flex-col justify-center p-6">
          <a
            v-if="article.category"
            class="text-blue-700 text-sm font-bold uppercase pb-4"
          >
            {{ article.category.title }}</a
          >
          <a class="text-3xl font-bold hover:text-gray-700 pb-4">{{
            article.title
          }}</a>
          <p class="text-sm pb-8">
            By
            <a class="font-semibold hover:text-gray-800">{{
              article.author
            }}</a>
            , Published on {{ article.created_time }}
          </p>
          <!-- <h1 class="text-2xl font-bold pb-3">Introduction</h1> -->
          <div class="md-e">
            <md-editor
              v-model="article.content"
              :preview-theme="theme"
              :previewOnly="true"
              @onGetCatalog="onGetCatalog"
            />
          </div>
        </div>
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

      <div
        class="w-full flex flex-col text-center md:text-left md:flex-row shadow bg-white mt-10 mb-10 p-6"
      >
        <div class="w-full md:w-1/5 flex justify-center md:justify-start pb-4">
          <img
            src="https://img.paulzzh.com/touhou/random"
            class="rounded-full shadow h-32 w-32"
          />
        </div>
        <div class="flex-1 flex flex-col justify-center md:justify-start">
          <p class="font-semibold text-2xl">David</p>
          <p class="pt-2">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur
            vel neque non libero suscipit suscipit eu eu urna.
          </p>
          <div
            class="flex items-center justify-center md:justify-start text-2xl no-underline text-blue-800 pt-4"
          >
            <a class href="#">
              <i class="fab fa-facebook"></i>
            </a>
            <a class="pl-4" href="#">
              <i class="fab fa-instagram"></i>
            </a>
            <a class="pl-4" href="#">
              <i class="fab fa-twitter"></i>
            </a>
            <a class="pl-4" href="#">
              <i class="fab fa-linkedin"></i>
            </a>
          </div>
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
            class="flex space-y-3 items-center
            md:flex-col md:justify-center md:space-x-0 md:space-y-3  
            lg:flex-row lg:space-y-0 lg:justify-between lg:space-x-12 
            sm:flex-row sm:space-y-0 sm:justify-between sm:space-x-12
            xs:flex-row sm:space-y-0 xs:justify-between sm:space-x-12"
          >
            <div class="flex items-center align-center md:mt-2 lg:mt-0">
              <img
                src="https://img.paulzzh.com/touhou/random"
                alt="avatar"
                class="object-cover w-8 h-8 rounded-full"
              />
              <a class="mx-3 text-sm text-gray-700 hover:underline">{{
                a.author
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
        <div id="boxFixed"><br /></div>
      </div>
      <div
        class="bg-white mt-4 p-2 xs:hidden 
        sm:hidden md:block lg:block boxFixed
        shadow"
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
} from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import MdEditor from "md-editor-v3";
import "md-editor-v3/lib/style.css";
export default {
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  components: { MdEditor },
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
      offsetTop: 0,
      scrollTop: 0,
      isLoggedIn: computed(() => store.getters.isLoggedIn),
    });
    const getArticle = (slug = props.slug) => {
      fetch(`/api/blog/${slug}/`, {
        method: "GET",
        headers: {
          "Content-Type": "Application/json",
          "X-CSRFTOKEN": Cookies.get("csrftoken"),
          Authorization: "Token " + state.isLoggedIn,
        },
      })
        .then((response) => response.json())
        .then((data) => {
          // console.log(data);
          state.article = data;
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
      state.isFixed = scrollTop > state.offsetTop + offset ? true : false;
    };
    onMounted(() => {
      window.addEventListener("scroll", initHeight);
      nextTick(() => {
        //获取对象相对于版面或由 offsetTop 属性指定的父坐标的计算顶端位置
        state.offsetTop = document.querySelector("#boxFixed").offsetTop;
      });
    });
    onUnmounted(() => {
      window.removeEventListener("scroll", initHeight);
    });
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
</style>
