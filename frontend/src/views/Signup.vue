<template>
  <div
    class="relative min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 bg-no-repeat"
    style="background-image: url(https://images.unsplash.com/photo-1525302220185-c387a117886e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80);"
  >
    <div class="absolute bg-black opacity-60 inset-0 z-0"></div>
    <div class="max-w-md w-full space-y-8 p-10 bg-white rounded-xl z-10">
      <div class="text-center">
        <h2 class="mt-6 text-3xl font-bold text-gray-900">Register an account!</h2>
        <p class="mt-2 text-sm text-gray-600">Please sign up to your account</p>
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
          <label class="text-sm font-bold text-gray-700 tracking-wide">Username</label>
          <input
            class="w-full text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type
            placeholder="Enter your Username"
            v-model="username"
          />
          <p v-show="Rusername" class="text-sm text-red-400">{{ Rusername }}</p>
        </div>
        <div class="mt-8 content-center">
          <label class="text-sm font-bold text-gray-700 tracking-wide">Email</label>
          <input
            class="w-full text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type
            placeholder="Enter your e-mail"
            v-model="email"
          />
          <p v-show="Remail" class="text-sm text-red-400">{{ Remail }}</p>
        </div>
        <div class="mt-8 content-center">
          <label class="text-sm font-bold text-gray-700 tracking-wide">Password1</label>
          <input
            class="w-full content-center text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type="password"
            placeholder="Enter your password"
            v-model="password1"
          />
          <p v-show="Rpassword1" class="text-sm text-red-400">{{ Rpassword1 }}</p>
        </div>
        <div class="mt-8 content-center">
          <label class="text-sm font-bold text-gray-700 tracking-wide">Password2</label>
          <input
            class="w-full content-center text-base py-2 border-b border-gray-300 focus:outline-none focus:border-indigo-500"
            type="password"
            placeholder="Enter your password again"
            v-model="password2"
          />
          <p v-show="Rpassword2" class="text-sm text-red-400">{{ Rpassword2 }}</p>
        </div>

        <div>
          <button
            type="submit"
            class="w-full flex justify-center bg-indigo-500 text-gray-100 p-4 rounded-full tracking-wide font-semibold focus:outline-none focus:shadow-outline hover:bg-indigo-600 shadow-lg cursor-pointer transition ease-in duration-300"
          >Sign up</button>
        </div>
        <p
          class="flex flex-col items-center justify-center mt-10 text-center text-md text-gray-500"
        >
          <span>Already had an account?</span>
          <router-link
            to="/login"
            href="#"
            class="text-indigo-500 hover:text-indigo-500no-underline hover:underline cursor-pointer transition ease-in duration-300"
          >Sign in</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { reactive, toRefs } from 'vue'
import { useRouter } from 'vue-router'
import Cookies from 'js-cookie'
import { createToast } from 'mosha-vue-toastify'
import "mosha-vue-toastify/dist/style.css"

export default {
  name: '',
  setup() {
    const router = useRouter()
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
    })
    return {
      ...toRefs(state),
      handleSignup: () => {
        state.Rusername = ''
        state.Remail = ''
        state.Rpassword1 = ''
        state.Rpassword2 = ''
        axios.post("/rest-auth/registration/",
          {
            username: state.username,
            email: state.email,
            password1: state.password1,
            password2: state.password2
          },
          {
            headers: {
              "X-CSRFTOKEN": Cookies.get('csrftoken'),
              "Content-Type": "application/json"
            }
          }
        )
          .then(
            res => {
              if (res.data.detail) {
                createToast({
                  title: res.data.detail
                },
                  {
                    position: 'bottom-right',
                    type: 'danger'
                  })
              } else if (res.data.key) {
                createToast({
                  title: "Register Successfully",
                  description: "Now going to login page!"
                },
                  {
                    position: 'bottom-right',
                    type: 'default',
                    timeout: 2000,
                  }
                )
                setTimeout(() => { router.push({ name: "login" }) }, 2000)
              }
            }
          )
          .catch(e => {
            if (e.response) {
              state.Rusername = e.response.data.username ? e.response.data.username[0] : ""
              state.Remail = e.response.data.email ? e.response.data.email[0] : ""
              state.Rpassword1 = e.response.data.password1 ? e.response.data.password1[0] : ""
              state.Rpassword2 = e.response.data.password2 ? e.response.data.password2[0] : ""
              if (e.response.data.detail) {
                state.detail = e.response.data.detail
              } else if (e.response.data.non_field_errors) {
                state.detail = e.response.data.non_field_errors[0]
              }
              if (state.detail) {
                createToast({
                  title: state.detail
                },
                  {
                    position: 'bottom-right',
                    type: 'danger',
                    showIcon: true,
                  })

              }
            } else if (e.request) {
              console.log(e.request)
            } else {
              console.log(e.message)
            }
          })
      },
    }
  }
}
</script>
