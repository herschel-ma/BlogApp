<template>
  <div
    class="relative min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 bg-no-repeat"
    style="background-image: url(https://images.unsplash.com/photo-1525302220185-c387a117886e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80);"
  >
    <div class="absolute bg-black opacity-60 inset-0 z-0"></div>
    <div class="max-w-md w-full space-y-8 p-10 bg-white rounded-xl z-10">
      <div class="text-center">
        <h2 class="mt-6 text-3xl font-bold text-gray-900">欢迎回来~</h2>
        <p class="mt-2 text-sm text-gray-600">请登录你的账户</p>
        <p class="mt-2 text-sm text-red-300">当前仅支持github授权登录</p>
      </div>
      <div class="flex flex-row justify-center items-center space-x-3">
        <span
          class="w-11 h-11 items-center justify-center inline-flex rounded-full font-bold text-lg text-white bg-blue-900 hover:shadow-lg cursor-pointer transition ease-in duration-300"
        >
          <img
            class="w-4 h-4"
            src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDI0IDI0IiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MTIgNTEyIiB4bWw6c3BhY2U9InByZXNlcnZlIiBjbGFzcz0iIj48Zz48cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGQ9Im0xNS45OTcgMy45ODVoMi4xOTF2LTMuODE2Yy0uMzc4LS4wNTItMS42NzgtLjE2OS0zLjE5Mi0uMTY5LTMuMTU5IDAtNS4zMjMgMS45ODctNS4zMjMgNS42Mzl2My4zNjFoLTMuNDg2djQuMjY2aDMuNDg2djEwLjczNGg0LjI3NHYtMTAuNzMzaDMuMzQ1bC41MzEtNC4yNjZoLTMuODc3di0yLjkzOWMuMDAxLTEuMjMzLjMzMy0yLjA3NyAyLjA1MS0yLjA3N3oiIGZpbGw9IiNmZmZmZmYiIGRhdGEtb3JpZ2luYWw9IiMwMDAwMDAiIHN0eWxlPSIiIGNsYXNzPSIiPjwvcGF0aD48L2c+PC9zdmc+"
          />
        </span>
        <span
          class="w-11 h-11 items-center justify-center inline-flex rounded-full font-bold text-lg text-white bg-blue-400 hover:shadow-lg cursor-pointer transition ease-in duration-300"
        >
          <img
            class="w-4 h-4"
            src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDY4MS4zMzQ2NCA2ODEiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiPjxnPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTIwMC45NjQ4NDQgNTE1LjI5Mjk2OWMyNDEuMDUwNzgxIDAgMzcyLjg3MTA5NC0xOTkuNzAzMTI1IDM3Mi44NzEwOTQtMzcyLjg3MTA5NCAwLTUuNjcxODc1LS4xMTcxODgtMTEuMzIwMzEzLS4zNzEwOTQtMTYuOTM3NSAyNS41ODU5MzctMTguNSA0Ny44MjQyMTgtNDEuNTg1OTM3IDY1LjM3MTA5NC02Ny44NjMyODEtMjMuNDgwNDY5IDEwLjQ0MTQwNi00OC43NTM5MDcgMTcuNDYwOTM3LTc1LjI1NzgxMyAyMC42MzY3MTggMjcuMDU0Njg3LTE2LjIzMDQ2OCA0Ny44MjgxMjUtNDEuODk0NTMxIDU3LjYyNS03Mi40ODgyODEtMjUuMzIwMzEzIDE1LjAxMTcxOS01My4zNjMyODEgMjUuOTE3OTY5LTgzLjIxNDg0NCAzMS44MDg1OTQtMjMuOTE0MDYyLTI1LjQ3MjY1Ni01Ny45NjQ4NDMtNDEuNDAyMzQ0LTk1LjY2NDA2Mi00MS40MDIzNDQtNzIuMzY3MTg4IDAtMTMxLjA1ODU5NCA1OC42ODc1LTEzMS4wNTg1OTQgMTMxLjAzMTI1IDAgMTAuMjg5MDYzIDEuMTUyMzQ0IDIwLjI4OTA2MyAzLjM5ODQzNyAyOS44ODI4MTMtMTA4LjkxNzk2OC01LjQ4MDQ2OS0yMDUuNTAzOTA2LTU3LjYyNS0yNzAuMTMyODEyLTEzNi45MjE4NzUtMTEuMjUgMTkuMzYzMjgxLTE3Ljc0MjE4OCA0MS44NjMyODEtMTcuNzQyMTg4IDY1Ljg3MTA5MyAwIDQ1LjQ2MDkzOCAyMy4xMzY3MTkgODUuNjA1NDY5IDU4LjMxNjQwNyAxMDkuMDgyMDMyLTIxLjUtLjY2MDE1Ni00MS42OTUzMTMtNi41NjI1LTU5LjM1MTU2My0xNi4zODY3MTktLjAxOTUzMS41NTA3ODEtLjAxOTUzMSAxLjA4NTkzNy0uMDE5NTMxIDEuNjcxODc1IDAgNjMuNDY4NzUgNDUuMTcxODc1IDExNi40NjA5MzggMTA1LjE0NDUzMSAxMjguNDY4NzUtMTEuMDE1NjI1IDIuOTk2MDk0LTIyLjYwNTQ2OCA0LjYwOTM3NS0zNC41NTg1OTQgNC42MDkzNzUtOC40Mjk2ODcgMC0xNi42NDg0MzctLjgyODEyNS0yNC42MzI4MTItMi4zNjMyODEgMTYuNjgzNTk0IDUyLjA3MDMxMiA2NS4wNjY0MDYgODkuOTYwOTM3IDEyMi40MjU3ODEgOTEuMDIzNDM3LTQ0Ljg1NTQ2OSAzNS4xNTYyNS0xMDEuMzU5Mzc1IDU2LjA5NzY1Ny0xNjIuNzY5NTMxIDU2LjA5NzY1Ny0xMC41NjI1IDAtMjEuMDAzOTA2LS42MDU0NjktMzEuMjYxNzE4OC0xLjgxNjQwNyA1Ny45OTk5OTk4IDM3LjE3NTc4MSAxMjYuODcxMDkzOCA1OC44NzEwOTQgMjAwLjg4NjcxODggNTguODcxMDk0IiBmaWxsPSIjZmZmZmZmIiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIj48L3BhdGg+PC9nPjwvc3ZnPg=="
          />
        </span>
        <span
          @click="getGithubCode"
          class="w-11 h-11 items-center justify-center inline-flex rounded-full font-bold text-lg text-white bg-blue-500 hover:shadow-lg cursor-pointer transition ease-in duration-300"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            viewBox="0 0 24 24"
          >
            <path
              d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
            />
          </svg>
        </span>
      </div>
      <div class="flex items-center justify-center space-x-2">
        <span class="h-px w-16 bg-gray-300"></span>
        <span class="text-gray-500 font-normal">或者</span>
        <span class="h-px w-16 bg-gray-300"></span>
      </div>
      <form class="mt-8 space-y-6" method="POST" @submit.prevent="handleSignIn">
        <div class="relative">
          <div class="absolute right-0 mt-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6 text-green-500"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <label class="text-sm font-bold text-gray-700 tracking-wide"
            >您的昵称</label
          >
          <input
            class="w-full text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type
            placeholder="写下您的昵称"
            v-model="user.username"
          />
        </div>
        <div class="mt-8 content-center">
          <label class="text-sm font-bold text-gray-700 tracking-wide"
            >您的密码</label
          >
          <input
            class="w-full content-center text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type="password"
            placeholder="写下您的密码"
            v-model="user.password"
          />
        </div>
        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember_me"
              name="remember_me"
              type="checkbox"
              class="h-4 w-4 bg-indigo-500 focus:ring-indigo-400 border-gray-300 rounded"
            />
            <label for="remember_me" class="ml-2 block text-sm text-gray-900"
              >记住我</label
            >
          </div>
          <div class="text-sm">
            <a
              @click="toggleModal"
              class="font-medium cursor-pointer text-indigo-500 hover:text-indigo-500"
              >忘记密码?</a
            >
          </div>
        </div>
        <div>
          <button
            type="submit"
            class="w-full flex justify-center bg-indigo-500 text-gray-100 p-4 rounded-full tracking-wide font-semibold focus:outline-none focus:shadow-outline hover:bg-indigo-600 shadow-lg cursor-pointer transition ease-in duration-300"
          >
            登录
          </button>
        </div>
        <p
          class="flex flex-col items-center justify-center mt-10 text-center text-md text-gray-500"
        >
          <span>没有账号吗?</span>
          <router-link
            to="/signup"
            class="text-indigo-500 hover:text-indigo-500no-underline hover:underline cursor-pointer transition ease-in duration-300"
            >去注册</router-link
          >
        </p>
      </form>
    </div>
  </div>
  <ModalDialog :show="showModal" @close="showModal = false" class="z-50">
    <template v-slot:innerForm>
      <div
        class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto"
      >
        <div class="modal-content py-4 text-left px-6">
          <div class="flex justify-center items-center pb-3">
            <p class="text-2xl font-bold text-center">重置密码</p>
          </div>

          <form class="mt-6" method="POST" @submit.prevent="handleSubmitEmail">
            <div>
              <label
                for="old_password"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >您注册的邮箱：</label
              >
              <input
                id="email"
                type="email"
                v-model="email"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <p v-show="Remail" class="text-sm text-red-400">
                {{ Remail }}
              </p>
            </div>
            <div class="mt-6">
              <button
                type="submit"
                class="flex items-center justify-center w-full px-6 py-2 text-sm font-medium text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:bg-blue-400 focus:outline-none"
              >
                <span class="m-2 text-white">
                  发送邮件
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
import { reactive, toRefs, computed } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import axios from "axios";
import Cookies from "js-cookie";
import ModalDialog from "@/components/ModalDialog";
export default {
  name: "Login",
  components: { ModalDialog },
  setup() {
    const user = reactive({
      username: "",
      password: "",
    });
    const state = reactive({
      email: "",
      Remail: "",
      showModal: false,
      detail: "",
      isLoggedIn: computed(() => store.getters.isLoggedIn),
    });
    const store = useStore();
    const router = useRouter();
    const toast = useToast();
    // 使用actions
    const getGithubCode = () => {
      router.replace({ name: "github" });
    };
    const toggleModal = () => {
      state.showModal = !state.showModal;
    };
    const handleSubmitEmail = () => {
      axios
        .post(
          `/rest-auth/password/reset/`,
          {
            email: state.email,
          },
          {
            headers: {
              "Content-Type": "Application/json",
              "X-CSRFTOKEN": Cookies.get("csrftoken"),
              Authorization: "Token " + state.isLoggedIn,
            },
          }
        )
        .then((response) => {
          toast.success(response.data.detail, { timeout: 2000 });
          state.showModal = !state.showModal;
        })
        .catch((e) => {
          if (e.response) {
            state.Remail = e.response.data.email
              ? e.response.data.email[0]
              : "";
            if (e.response.data.detail) {
              state.detail = e.response.data.detail;
            } else if (e.response.data.non_field_errors) {
              state.detail = e.response.data.non_field_errors[0];
            }
            if (state.detail) {
              toast.error(state.detail, { timeout: 2000 });
            }
          }
        });
    };
    return {
      ...toRefs(state),
      handleSignIn: () => store.dispatch("login", user),
      user,
      getGithubCode,
      toggleModal,
      handleSubmitEmail,
    };
  },
};
</script>
