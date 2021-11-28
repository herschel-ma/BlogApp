<template>
  <form
    class="flex flex-col justify-between ml-5"
    method="POST"
    @submit.prevent="handleCreate"
  >
    <label class="text-gray-600 font-light">Title:</label>
    <input
      type="text"
      placeholder="Enter your input here"
      class="w-1/2 px-3 py-2 border rounded-lg text-gray-700 focus:outline-none focus:border-green-500"
      v-model="title"
    />
    <label class="text-gray-600 font-light">Content:</label>
    <md-editor v-model="content" :preview-theme="theme" />
    <button
      type="submit"
      class="w-40 flex justify-center bg-indigo-500 text-gray-100 p-4 rounded-full tracking-wide font-semibold focus:outline-none focus:shadow-outline hover:bg-indigo-600 shadow-lg cursor-pointer transition ease-in duration-300"
    >
      submit
    </button>
  </form>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";
import { reactive, toRefs } from "vue";
import { useToast } from "vue-toastification";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import MdEditor from "md-editor-v3";
import "md-editor-v3/lib/style.css";

export default {
  components: { MdEditor },
  setup() {
    const state = reactive({
      title: "",
      content: "",
      theme: "default",
    });
    const store = useStore();
    const router = useRouter();
    const toast = useToast();
    return {
      ...toRefs(state),
      toast,
      handleCreate: () => {
        axios
          .post(
            "/api/blog/",
            {
              title: state.title,
              content: state.content,
            },
            {
              headers: {
                "content-type": "application/json",
                "X-CSRFTOKEN": Cookies.get("csrftoken"),
                Authorization: "Token " + store.state.isLoggedIn,
              },
            }
          )
          .then((resp) => {
            if (resp.data.title) {
              toast.success("文章创建成功", { timeout: 2000 });
              setTimeout(() => {
                router.push({ name: "home" });
              }, 2000);
            }
          })
          .catch((e) => {
            if (e.response) {
              if (e.response.data.detail) {
                toast.error(e.response.data.detail, { timeout: 3000 });
              }
            } else {
              console.log(e);
            }
          });
      },
    };
  },
};
</script>

<style>
code {
  color: #f66;
}
</style>
