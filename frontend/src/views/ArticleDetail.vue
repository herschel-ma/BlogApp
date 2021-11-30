<template>
  <div class="container mx-auto flex flex-wrap py-6">
    <!-- Post Section -->
    <section class="w-full md:w-2/3 flex flex-col items-center px-3">
      <article class="flex flex-col shadow my-4">
        <!-- Article Image -->
        <a href="#" class="hover:opacity-75">
          <img src="https://img.paulzzh.com/touhou/random" />
        </a>
        <div class="bg-white flex flex-col justify-start p-6">
          <a href="#" class="text-blue-700 text-sm font-bold uppercase pb-4"
            >Technology</a
          >
          <a href="#" class="text-3xl font-bold hover:text-gray-700 pb-4">{{
            article.title
          }}</a>
          <p href="#" class="text-sm pb-8">
            By
            <a href="#" class="font-semibold hover:text-gray-800">{{
              article.author
            }}</a>
            , Published on {{ article.created_time }}
          </p>
          <!-- <h1 class="text-2xl font-bold pb-3">Introduction</h1> -->
          <md-editor
            v-model="article.content"
            :preview-theme="theme"
            :previewOnly="true"
          />
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
    <aside class="w-full md:w-1/3 flex flex-col items-center px-3">
      <div class="w-full bg-white shadow flex flex-col my-4 p-6">
        <p class="text-xl font-semibold pb-5">About Us</p>
        <p class="pb-2">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas
          mattis est eu odio sagittis tristique. Vestibulum ut finibus leo. In
          hac habitasse platea dictumst.
        </p>
        <a
          href="#"
          class="w-full bg-blue-800 text-white font-bold text-sm uppercase rounded hover:bg-blue-700 flex items-center justify-center px-2 py-3 mt-4"
          >关于我们</a
        >
      </div>
      <div class="w-full bg-white shadow flex flex-col my-4 p-6">
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
          href="#"
          class="w-full bg-blue-800 text-white font-bold text-sm uppercase rounded hover:bg-blue-700 flex items-center justify-center px-2 py-3 mt-6"
        >
          <i class="fab fa-instagram"></i> Follow @dgrzyb
        </a>
      </div>
    </aside>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import axios from "axios";
import { reactive, toRefs } from "vue";
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
    // 监听路由变化获取上一章下一章内容
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
      theme: "default",
      messagePrev: null,
      messageNext: null,
      prevSlug: "",
      nextSlug: "",
    });
    const getArticle = (slug = props.slug) => {
      fetch(`/api/blog/${slug}/`, {
        method: "GET",
        headers: {
          "Content-Type": "Application/json",
          "X-CSRFTOKEN": Cookies.get("csrftoken"),
          Authorization: "Token " + store.state.isLoggedIn,
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
            Authorization: "Token " + store.state.isLoggedIn,
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
            Authorization: "Token " + store.state.isLoggedIn,
          },
        })
        .then((res) => {
          state.messageNext = res.data.message || res.data.title;
          state.nextSlug = res.data.slug || props.slug;
        })
        .catch((e) => {
          console.log(e.response.message);
        });
    };
    getArticle();
    getPrevNext();

    return {
      ...toRefs(state),
      router,
      getArticle,
      getPrevNext,
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
    };
  },
};
</script>
