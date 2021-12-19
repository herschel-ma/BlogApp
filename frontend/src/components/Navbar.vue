<template>
  <!-- navbar goes here -->
  <nav class="bg-gray-400">
    <div class="mx-auto px-2">
      <div class="flex justify-between items-center">
        <div class="flex space-x-3">
          <!-- logo -->
          <div>
            <a
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
              <router-link to="/" class="font-bold">首页</router-link>
            </a>
          </div>
          <!-- primary nav -->
          <div v-if="loggedIn" class="hidden md:flex space-x-5 items-center">
            <router-link
              :to="{ name: 'history' }"
              class="py-5 text-gray-700 hover:text-blue-500"
              >历史上的今天</router-link
            >
            <router-link
              :to="{ name: 'archive' }"
              class="py-5 text-gray-700 hover:text-blue-500"
              >归档</router-link
            >
            <router-link to="/" class="py-5 text-gray-700 hover:text-blue-500"
              >友链</router-link
            >
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
            class="py-2 px-3 bg-yellow-400 hover:bg-yellow-300 text-yellow-700 hover:text-yellow-800 rounded transition duration-100"
            >注册</router-link
          >
        </div>
        <div v-else class="hidden md:flex space-x-2 items-center mr-3">
          <div class="relative flex items-center">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="absolute right-0 w-6 h-6 mr-2 text-yellow-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
            <input
              type="text"
              :placeholder="searchPlaceholder"
              @keyup.enter="search($event)"
              class="w-32 py-2 bg-gray-200 border-b-2 rounded-full border-gray-400 focus:border-yellow-400 outline-none"
            />
          </div>
          <a class="flex items-center mr-4 text-gray-700 hover:text-blue-500">
            <img
              :src="avatarUrl"
              alt="avatar"
              class="hidden object-cover w-10 h-10 mx-4 rounded-full sm:block"
            />
            <div class="relative">
              <!-- Dropdown toggle button -->
              <button
                @click="toggleProfile"
                class="flex items-center bg-gray-400 rounded-md"
              >
                <span class="mr-4">{{ userName }}</span>
                <svg
                  class="w-5 h-5 text-gray-800 dark:text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                    clip-rule="evenodd"
                  />
                </svg>
              </button>
              <!-- Dropdown List -->
              <div
                v-show="showDropDown"
                class="absolute right-0 top-6 py-1 mt-2 bg-gray-100 divide-y divide-gray-600 rounded-md shadow-xl text-center w-20"
              >
                <a
                  @click="toggleModal"
                  class="block cursor-pointer px-2 py-1 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
                >
                  修改密码
                </a>
                <a
                  @click="toggleChangeInfoModal"
                  class="block cursor-pointer px-2 py-1 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
                >
                  修改资料
                </a>
                <router-link
                  :to="{ name: 'create' }"
                  @click="showDropDown = false"
                  class="block cursor-pointer px-2 py-1 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
                  >新建博文</router-link
                >
              </div>
            </div>
          </a>
          <a
            @click="handleLogOut"
            class="cursor-pointer py-2 px-3 bg-red-200 hover:bg-red-300 text-gray-700 rounded hover:text-red-500 transition duration-100"
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
                <div class="tham-inner bg-green-700" />
              </div>
            </div>
          </button>
        </div>
      </div>
      <!-- mobile menu -->
      <transition name="collapse" class="flex flex-col justify-start">
        <div v-show="!hidden" class="column h-auto">
          <div v-if="!loggedIn">
            <router-link
              to="/login"
              @click="showMobileMenu"
              class="block py-2 px-4 text-sm hover:bg-gray-200"
              >登录</router-link
            >
            <router-link
              to="/signup"
              @click="showMobileMenu"
              class="block py-2 px-4 text-sm hover:bg-gray-200"
              >注册</router-link
            >
          </div>
          <div v-else>
            <div class="relative flex items-center ml-3 p-0 m-0">
              <input
                type="text"
                :placeholder="searchPlaceholder"
                @keyup.enter="search($event)"
                class="w-full p-0 px-3 m-0 border-gray-500 border-b-2 rounded-md bg-gray-400 outline-none"
              />
            </div>
            <router-link
              :to="{ name: 'history' }"
              @click="showMobileMenu"
              class="block py-2 px-4 text-sm hover:bg-gray-200"
              >历史上的今天</router-link
            >
            <router-link
              :to="{ name: 'archive' }"
              @click="showMobileMenu"
              class="block py-2 px-4 text-sm hover:bg-gray-200"
              >归档</router-link
            >
            <router-link
              to="/"
              @click="showMobileMenu"
              class="block py-2 px-4 text-sm hover:bg-gray-200"
              >友链</router-link
            >
            <div
              @click="showSubMenu = !showSubMenu"
              class="block py-2 px-4 text-sm hover:bg-gray-200"
            >
              个人中心
            </div>
            <ul
              v-show="showSubMenu"
              class="block py-2 px-4 text-sm hover:bg-gray-200"
            >
              <li
                @click="toggleModal"
                class="block cursor-pointer px-2 py-1 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
              >
                修改密码
              </li>
              <li
                @click="toggleChangeInfoModal"
                class="block cursor-pointer px-2 py-1 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
              >
                修改资料
              </li>
              <router-link
                :to="{ name: 'create' }"
                @click="showMobileMenu"
                class="block cursor-pointer px-2 py-1 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
                >新建博文</router-link
              >
              <li
                @click="handleLogOut"
                class="block cursor-pointer px-2 py-1 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
              >
                登出
              </li>
            </ul>
          </div>
        </div>
      </transition>
    </div>
  </nav>
  <!--content goes here-->
  <ModalDialog
    :show="showModal"
    @close="
      showModal = false;
      showDropDown = false;
    "
    class="z-50"
  >
    <template v-slot:innerForm>
      <div
        class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto"
      >
        <div class="modal-content py-4 text-left px-6">
          <div class="flex justify-center items-center pb-3">
            <p class="text-2xl font-bold text-center">修改密码</p>
          </div>

          <form
            class="mt-6"
            method="POST"
            @submit.prevent="handleChangePassword"
          >
            <div>
              <label
                for="old_password"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >之前的密码：</label
              >
              <input
                id="old_password"
                type="password"
                v-model="old_password"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <p v-show="Rold_password" class="text-sm text-red-400">
                {{ Rold_password }}
              </p>
            </div>
            <div>
              <label
                for="password1"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >新密码：</label
              >
              <input
                id="password1"
                type="password"
                v-model="new_password1"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <p v-show="Rnew_password1" class="text-sm text-red-400">
                {{ Rnew_password1 }}
              </p>
            </div>
            <div>
              <label
                for="password2"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >确认密码：</label
              >
              <input
                type="password"
                id="password2"
                v-model="new_password2"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <p v-show="Rnew_password2" class="text-sm text-red-400">
                {{ Rnew_password2 }}
              </p>
            </div>
            <div class="mt-6">
              <button
                type="submit"
                class="flex items-center justify-center w-full px-6 py-2 text-sm font-medium text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:bg-blue-400 focus:outline-none"
              >
                <span class="m-2 text-white">
                  修改密码
                </span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </template>
  </ModalDialog>
  <ModalDialog
    :show="showChangeInfoModal"
    @close="
      showChangeInfoModal = false;
      showDropDown = false;
    "
    class="z-50"
  >
    <template v-slot:innerForm>
      <div
        class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto"
      >
        <div class="modal-content py-4 text-left px-6">
          <div class="flex justify-center items-center pb-3">
            <p class="text-2xl font-bold text-center">修改资料</p>
          </div>

          <form>
            <!-- component -->
            <div
              class="flex w-full items-center justify-center bg-grey-lighter"
            >
              <label
                class="w-64 flex flex-col items-center px-4 py-6 bg-white text-blue rounded-lg shadow-lg tracking-wide uppercase border border-blue cursor-pointer"
              >
                <svg
                  class="w-8 h-8"
                  fill="currentColor"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M16.88 9.1A4 4 0 0 1 16 17H5a5 5 0 0 1-1-9.9V7a3 3 0 0 1 4.52-2.59A4.98 4.98 0 0 1 17 8c0 .38-.04.74-.12 1.1zM11 11h3l-4-4-4 4h3v3h2v-3z"
                  />
                </svg>
                <span class="mt-2 text-base leading-normal">上传头像</span>
                <input type="file" class="hidden" @change="onFileChange" />
              </label>
            </div>
          </form>
          <form class="mt-6" method="POST" @submit.prevent="hangleChangeInfo">
            <div>
              <label
                for="description"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >个人简介：</label
              >
              <textarea
                id="description"
                type="text"
                v-model="description"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <p v-show="Rdescription" class="text-sm text-red-400">
                {{ Rdescription }}
              </p>
            </div>
            <div class="mt-6">
              <button
                type="submit"
                class="flex items-center justify-center w-full px-6 py-2 text-sm font-medium text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:bg-blue-400 focus:outline-none"
              >
                <span class="m-2 text-white">
                  修改资料
                </span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </template>
  </ModalDialog>
</template>

<script>
import axios from "axios";
import { reactive, computed, onMounted, toRefs } from "vue";
import { useStore } from "vuex";
import { useToast } from "vue-toastification";
import Cookies from "js-cookie";
import ModalDialog from "@/components/ModalDialog";
export default {
  name: "Navbar",
  components: { ModalDialog },
  setup() {
    const store = useStore();
    const toast = useToast();
    let loggedIn = computed(function() {
      return store.state.isLoggedIn;
    });
    const search = (event) => {
      store.dispatch("storeSearchWord", event.target.value);
      event.target.value = "";
      data.searchPlaceholder = "搜索";
      data.hidden = "hidden";
    };
    const toggleProfile = () => {
      data.showDropDown = !data.showDropDown;
    };
    onMounted(() => {
      store.dispatch("githubLoggedIn");
      getUserInfo();
    });

    const data = reactive({
      hidden: "hidden",
      userName: "",
      avatarUrl: "",
      showDropDown: false,
      showModal: false,
      isLoggedIn: computed(() => store.getters.isLoggedIn),
      old_password: "",
      new_password1: "",
      new_password2: "",
      detail: "",
      Rold_password: "",
      Rnew_password1: "",
      Rnew_password2: "",
      showChangeInfoModal: false,
      avatarId: 0,
      description: "",
      Rdescription: "",
      showSubMenu: false,
      searchPlaceholder: "搜索",
      timer: null,
      date: null,
    });
    const getUserInfo = () => {
      axios.get("/api/user/").then((response) => {
        data.userName = response.data.username;
        data.avatarId = response.data.id;
        data.description = response.data.description;
        store.dispatch("storeUserName", response.data.username);
        store.dispatch("storeUserId", response.data.id);
        if (response.data.user === null) {
          data.avatarUrl =
            response.data.avatar !== null
              ? response.data.avatar.content
              : "https://img.paulzzh.com/touhou/random";
        } else {
          data.avatarUrl = response.data.user.avatar_url;
        }
      });
    };
    const toggleModal = () => {
      data.showModal = !data.showModal;
    };
    const toggleChangeInfoModal = () => {
      data.showChangeInfoModal = !data.showChangeInfoModal;
    };
    const handleChangePassword = () => {
      axios
        .post(
          `/rest-auth/password/change/`,
          {
            old_password: data.old_password,
            new_password1: data.new_password1,
            new_password2: data.new_password2,
          },
          {
            headers: {
              "Content-Type": "Application/json",
              "X-CSRFTOKEN": Cookies.get("csrftoken"),
              Authorization: "Token " + data.isLoggedIn,
            },
          }
        )
        .then((response) => {
          toast.success(response.data.detail, { timeout: 2000 });
          data.showModal = !data.showModal;
          data.showDropDown = !data.showDropDown;
          data.hidden = data.hidden == "" ? "hidden" : "";
        })
        .catch((e) => {
          if (e.response) {
            data.Rold_password = e.response.data.old_password
              ? e.response.data.old_password[0]
              : "";
            data.Rnew_password1 = e.response.data.new_password1
              ? e.response.data.new_password1[0]
              : "";
            data.Rnew_password2 = e.response.data.new_password2
              ? e.response.data.new_password2[0]
              : "";
            if (e.response.data.detail) {
              data.detail = e.response.data.detail;
            } else if (e.response.data.non_field_errors) {
              data.detail = e.response.data.non_field_errors[0];
            }
            if (data.detail) {
              toast.error(data.detail, { timeout: 2000 });
            }
          }
        });
    };
    const onFileChange = (e) => {
      const file = e.target.files[0];
      let formData = new FormData();
      formData.append("content", file);
      axios
        .post(`/api/avatar/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + data.isLoggedIn,
          },
        })
        .then((res) => {
          data.avatarId = res.data.id;
          toast.success("上传头像成功", { timeout: 2000 });
        })
        .catch((error) => console.log(error));
    };
    const hangleChangeInfo = () => {
      axios
        .put(
          `/api/user/`,
          {
            description: data.description,
            avatar_id: data.avatarId,
          },
          {
            headers: {
              "Content-Type": "application/json",
              "X-CSRFTOKEN": Cookies.get("csrftoken"),
              Authorization: "Token " + data.isLoggedIn,
            },
          }
        )
        .then((res) => {
          getUserInfo();
          data.showChangeInfoModal = false;
          data.showDropDown = false;
          data.hidden = "hidden";
          toast.success(res.data.detail, { timeout: 2000 });
        })
        .catch((error) => {
          if (error.response.data.detail) {
            toast.error(error.response.data.detail, { timeout: 2000 });
          }
        });
    };
    return {
      ...toRefs(data),
      showMobileMenu: () => (data.hidden = data.hidden == "" ? "hidden" : ""),
      handleLogOut: () => {
        data.hidden = "hidden";
        store.dispatch("logout");
      },
      loggedIn,
      search,
      toggleProfile,
      toggleModal,
      handleChangePassword,
      toggleChangeInfoModal,
      onFileChange,
      hangleChangeInfo,
    };
  },
};
</script>

<style>
.collapse-enter-active {
  transition: opacity 2s;
}
.collapse-leave-active {
  transition: opacity 0.5s;
}
.collapse-enter,
.collapse-leave-to {
  opacity: 0;
}
</style>
