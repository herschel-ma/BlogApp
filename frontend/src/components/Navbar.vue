<template>
  <!-- navbar goes here -->
  <nav class="bg-gray-400">
    <div class="max-w-7xl mx-auto px-2">
      <div class="flex justify-between">
        <div class="flex space-x-3">
          <!-- logo -->
          <div>
            <a
              href="#"
              class="flex items-center py-5 px-3 text-gray-600 hover:text-blue-500"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mt-1 mr-2 text-red-400 hover:text-red-500 animate-bounce"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z"
                  clip-rule="evenodd"
                />
              </svg>
              <router-link to="/" class="font-bold">主页</router-link>
            </a>
          </div>
          <!-- primary nav -->
          <div class="hidden md:flex space-x-5 items-center">
            <router-link
              v-if="loggedIn"
              :to="{ name: 'create' }"
              href="#"
              class="py-5 px-2 text-gray-700 hover:text-blue-500"
              >新建博文</router-link
            >
            <a href="#" class="text-gray-700 hover:text-blue-500">项目</a>
          </div>
        </div>
        <!-- secordary nav -->
        <div
          v-if="!loggedIn"
          class="hidden md:flex space-x-2 items-center mr-3"
        >
          <router-link
            to="/login"
            class="py-5 px-4 text-gray-700 hover:text-blue-500"
            >登录</router-link
          >
          <router-link
            to="/signup"
            href="#"
            class="py-2 px-3 bg-yellow-400 hover:bg-yellow-300 text-yellow-700 hover:text-yellow-800 rounded transition duration-100"
            >注册</router-link
          >
        </div>
        <div v-else class="hidden md:flex space-x-2 items-center mr-3">
          <a
            href="#"
            class="flex items-center mr-4 text-gray-700 hover:text-blue-500"
          >
            <img
              :src="avatarUrl"
              alt="avatar"
              class="hidden object-cover w-10 h-10 mx-4 rounded-full sm:block"
            />
            <p>{{ userName }}</p>
          </a>
          <a
            herf="#"
            @click="handleLogOut"
            class="py-2 px-3 bg-red-200 hover:bg-red-300 text-gray-700 rounded hover:text-red-500 transition duration-100"
            >登出</a
          >
        </div>
        <!-- mobile button goes here -->
        <div class="md:hidden flex items-center">
          <button @click="showMobileMenu">
            <div
              class="tham tham-e-spin tham-w-8"
              :class="{ 'tham-active': !hidden }"
            >
              <div class="tham-box">
                <div class="tham-inner bg-purple-500" />
              </div>
            </div>
          </button>
        </div>
      </div>
      <!-- mobile menu -->
      <div :class="hidden">
        <router-link
          to="/post"
          class="block py-2 px-4 text-sm hover:bg-gray-200"
          >Blog</router-link
        >
        <router-link
          to="/post"
          class="block py-2 px-4 text-sm hover:bg-gray-200"
          >Projects</router-link
        >
        <router-link
          to="/post"
          class="block py-2 px-4 text-sm hover:bg-gray-200"
          >Friendly Link</router-link
        >
        <router-link
          to="/login"
          @click="showMobileMenu"
          class="block py-2 px-4 text-sm hover:bg-gray-200"
          >Login</router-link
        >
      </div>
    </div>
  </nav>
  <!--content goes here-->
</template>

<script>
import axios from "axios";
import { reactive, computed, onMounted, toRefs } from "vue";
import { useStore } from "vuex";
export default {
  name: "Navbar",
  setup() {
    const store = useStore();
    let loggedIn = computed(function() {
      return store.state.isLoggedIn;
    });
    onMounted(() => {
      store.dispatch("githubLoggedIn");
      axios.get("/api/user/").then((response) => {
        data.userName = response.data.username;
        data.avatarUrl =
          response.data.user !== null
            ? response.data.user.avatar_url
            : "https://img.paulzzh.com/touhou/random";
      });
    });
    const data = reactive({
      hidden: "hidden",
      userName: "",
      avatarUrl: "",
    });
    return {
      ...toRefs(data),
      showMobileMenu: () => (data.hidden = data.hidden == "" ? "hidden" : ""),
      handleLogOut: () => store.dispatch("logout"),
      loggedIn,
    };
  },
};
</script>
