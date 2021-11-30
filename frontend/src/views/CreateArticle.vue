<template>
  <form
    class="flex flex-col justify-between ml-5"
    method="POST"
    @submit.prevent="handleCreate"
  >
    <label class="text-gray-600 font-light">标题:</label>
    <input
      type="text"
      placeholder="Enter your input here"
      class="w-1/2 px-3 py-2 border rounded-lg text-gray-700 focus:outline-none focus:border-green-500"
      v-model="title"
    />
    <label class="text-gray-600 font-light">内容:</label>
    <div class="flex space-x-1">
      <select
        class="w-3/7 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        @change="changeMDTheme($event)"
      >
        <option v-for="t in mdthemes" :value="t" :key="t"
          >编辑器主题切换为 {{ t }}
        </option>
      </select>
      <select
        class="w-4/7 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        @change="changeTheme($event)"
      >
        <option v-for="t in themes" :value="t" :key="t"
          >预览主题切换为 {{ t }}
        </option>
      </select>
    </div>
    <md-editor v-model="content" :preview-theme="theme" :theme="mdtheme" />
    <button
      type="submit"
      class="w-40 flex justify-center bg-indigo-500 text-gray-100 p-4 rounded-full tracking-wide font-semibold focus:outline-none focus:shadow-outline hover:bg-indigo-600 shadow-lg cursor-pointer transition ease-in duration-300"
    >
      提交并发布
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
      theme: "",
      mdtheme: "",
      themes: ["default", "github", "vuepress"],
      mdthemes: ["light", "dark"],
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
      changeTheme: (event) => {
        state.theme = event.target.value;
      },
      changeMDTheme: (event) => {
        state.mdtheme = event.target.value;
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
