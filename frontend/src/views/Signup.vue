<template>
  <div
    class="relative min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 bg-no-repeat"
    style="background-image: url(https://images.unsplash.com/photo-1525302220185-c387a117886e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80);"
  >
    <div class="absolute bg-black opacity-60 inset-0 z-0"></div>
    <div class="max-w-md w-full space-y-8 p-10 bg-white rounded-xl z-10">
      <div class="text-center">
        <h2 class="mt-6 text-3xl font-bold text-gray-900">
          注册
        </h2>
        <p class="mt-2 text-sm text-gray-600">注册一个属于你自己的账号</p>
      </div>
      <div class="flex items-center justify-center space-x-2"></div>
      <form class="mt-8 space-y-6" method="POST" @submit.prevent="handleSignup">
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
            placeholder="想一个昵称吧"
            v-model="username"
          />
          <p v-show="Rusername" class="text-sm text-red-400">{{ Rusername }}</p>
        </div>
        <div class="mt-8 content-center">
          <label class="text-sm font-bold text-gray-700 tracking-wide"
            >您的邮箱</label
          >
          <input
            class="w-full text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type
            placeholder="输入你的邮箱"
            v-model="email"
          />
          <p v-show="Remail" class="text-sm text-red-400">{{ Remail }}</p>
        </div>
        <div class="mt-8 content-center">
          <label class="text-sm font-bold text-gray-700 tracking-wide">
            您的密码
          </label>
          <input
            class="w-full content-center text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type="password"
            placeholder="非礼勿视"
            v-model="password1"
          />
          <p v-show="Rpassword1" class="text-sm text-red-400">
            {{ Rpassword1 }}
          </p>
        </div>
        <div class="mt-8 content-center">
          <label class="text-sm font-bold text-gray-700 tracking-wide"
            >确认密码</label
          >
          <input
            class="w-full content-center text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type="password"
            placeholder="非礼勿视"
            v-model="password2"
          />
          <p v-show="Rpassword2" class="text-sm text-red-400">
            {{ Rpassword2 }}
          </p>
        </div>

        <div>
          <button
            type="submit"
            class="w-full flex justify-center bg-indigo-500 text-gray-100 p-4 rounded-full tracking-wide font-semibold focus:outline-none focus:shadow-outline hover:bg-indigo-600 shadow-lg cursor-pointer transition ease-in duration-300"
          >
            注册
          </button>
        </div>
        <p
          class="flex flex-col items-center justify-center mt-10 text-center text-md text-gray-500"
        >
          <span>已有账号?</span>
          <router-link
            to="/login"
            href="#"
            class="text-indigo-500 hover:text-indigo-500no-underline hover:underline cursor-pointer transition ease-in duration-300"
            >去登陆</router-link
          >
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { reactive, toRefs } from "vue";
import { useRouter } from "vue-router";
import Cookies from "js-cookie";
import { useToast } from "vue-toastification";

export default {
  setup() {
    const toast = useToast();
    const router = useRouter();
    const state = reactive({
      username: "",
      email: "",
      password1: "",
      password2: "",
      detail: "",
      Rusername: "",
      Remail: "",
      Rpassword1: "",
      Rpassword2: "",
    });
    return {
      ...toRefs(state),
      handleSignup: () => {
        state.Rusername = "";
        state.Remail = "";
        state.Rpassword1 = "";
        state.Rpassword2 = "";
        axios
          .post(
            "/rest-auth/registration/",
            {
              username: state.username,
              email: state.email,
              password1: state.password1,
              password2: state.password2,
            },
            {
              headers: {
                "X-CSRFTOKEN": Cookies.get("csrftoken"),
                "Content-Type": "application/json",
              },
            }
          )
          .then((res) => {
            if (res.data.detail) {
              toast.error(res.data.detail, { timeout: 3000 });
            } else if (res.data.key) {
              toast.success("注册成功", { timeout: 2000 });
              setTimeout(() => {
                router.push({ name: "login" });
              }, 2000);
            }
          })
          .catch((e) => {
            if (e.response) {
              state.Rusername = e.response.data.username
                ? e.response.data.username[0]
                : "";
              state.Remail = e.response.data.email
                ? e.response.data.email[0]
                : "";
              state.Rpassword1 = e.response.data.password1
                ? e.response.data.password1[0]
                : "";
              state.Rpassword2 = e.response.data.password2
                ? e.response.data.password2[0]
                : "";
              if (e.response.data.detail) {
                state.detail = e.response.data.detail;
              } else if (e.response.data.non_field_errors) {
                state.detail = e.response.data.non_field_errors[0];
              }
              if (state.detail) {
                toast.error(state.detail, { timeout: 2000 });
              }
            } else if (e.request) {
              console.log(e.request);
            } else {
              console.log(e.message);
            }
          });
      },
    };
  },
};
</script>
