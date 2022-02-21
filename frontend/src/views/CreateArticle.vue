<template>
  <div class="flex overflow-x-auto md:justify-center">
    <form
      class="flex flex-col justify-between md:mx-20 mx-2 "
      method="POST"
      @submit.prevent="handleCreatePost"
    >
      <label class="text-gray-600 font-light mt-5">标题:</label>
      <input
        type="text"
        placeholder="请输入文章标题"
        class="lg:w-1/2 px-3 py-2 mb-3 border border-gray-300 rounded-lg text-gray-700 focus:outline-none focus:border-indigo-300"
        v-model="title"
      />
      <p v-show="Rtitle" class="text-sm text-red-400 mb-2">{{ Rtitle }}</p>
      <div class="text-gray-600 font-light">分类:</div>
      <div
        class="md:grid md:grid-cols-5 md:gap-2 flex flex-wrap lg:flex lg:flex-wrap mb-2 item-center"
      >
        <span v-for="cate in categorys" :key="cate.id" class="mr-2">
          <button
            class="inline-block border px-6 py-2 mb-2 border-gray-300 rounded-md hover:border-red-300 text-base font-medium"
            :class="changeColor(cate)"
            @click.prevent="chooseCategory(cate)"
          >
            {{ cate.title }}
          </button>
        </span>
        <span>
          <button
            class="bg-green-500 mb-2 text-white rounded-md px-6 py-2 text-base font-medium hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-300"
            id="open-btn"
            @click.prevent="toggleModal"
          >
            创建分类
          </button>
        </span>
      </div>
      <p v-show="RcategoryId" class="text-sm text-red-400 mb-2">
        {{ RcategoryId }}
      </p>
      <label class="text-gray-600 font-light">标签:</label>
      <input
        type="text"
        placeholder="请输入文章标签，以逗号分隔"
        class="lg:w-1/2 px-3 py-2 mb-3 border border-gray-300 rounded-lg text-gray-700 focus:outline-none focus:border-indigo-300"
        v-model="tags"
      />
      <p v-show="Rtags.length > 0" class="text-sm text-red-400 mb-2">
        {{ Rtags }}
      </p>
      <label class="text-gray-600 font-light">摘要（非必须）:</label>
      <input
        type="text"
        placeholder="请输入摘要"
        class="lg:w-1/2 px-3 py-2 mb-3 border border-gray-300 rounded-lg text-gray-700 focus:outline-none focus:border-indigo-300"
        v-model="summery"
      />
      <label class="text-gray-600 font-light">内容:</label>
      <p v-show="Rcontent" class="text-sm text-red-400 mb-2">
        {{ Rcontent }}
      </p>
      <div class="flex flex-col">
        <select
          class="lg:w-1/2 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          @change="changeMDTheme($event)"
        >
          <option v-for="t in mdthemes" :value="t" :key="t"
            >编辑器主题切换为 {{ t }}
          </option>
        </select>
        <select
          class="lg:w-1/2 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          @change="changeTheme($event)"
        >
          <option v-for="t in themes" :value="t" :key="t"
            >预览主题切换为 {{ t }}
          </option>
        </select>
      </div>
      <div class="w-full">
        <md-editor
          v-model="content"
          :preview-theme="theme"
          :theme="mdtheme"
          class="mb-5"
          :onSave="handleCreatePost"
          @onUploadImg="handleUploadImg"
        />
      </div>
      <button
        type="submit"
        class="w-40 flex justify-center bg-indigo-500 text-gray-100 p-4 rounded-full tracking-wide font-semibold focus:outline-none focus:shadow-outline hover:bg-indigo-600 shadow-lg cursor-pointer transition ease-in duration-300"
      >
        创建并发布
      </button>
    </form>
  </div>
  <ModalDialog :show="showModal" @close="showModal = false">
    <template v-slot:innerForm>
      <div
        class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto"
      >
        <div class="modal-content py-4 text-left px-6">
          <div class="flex justify-center items-center pb-3">
            <p class="text-2xl font-bold text-center">创建分类</p>
          </div>

          <form class="mt-6" method="POST" @submit.prevent="handleCreateCate">
            <div>
              <label
                for="username"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >分类名：</label
              >
              <input
                type="text"
                v-model="cate"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
            </div>

            <div class="mt-6">
              <button
                type="submit"
                class="flex items-center justify-center w-full px-6 py-2 text-sm font-medium text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:bg-blue-400 focus:outline-none"
              >
                <span class="m-2  text-white" @click="close_modal()">
                  创建分类
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
import Cookies from "js-cookie";
import { reactive, toRefs, computed } from "vue";
import { useToast } from "vue-toastification";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import MdEditor from "md-editor-v3";
import "md-editor-v3/lib/style.css";
import ModalDialog from "@/components/ModalDialog";

export default {
  name: "CreateArticle",
  components: { MdEditor, ModalDialog },
  setup() {
    const state = reactive({
      title: "",
      content: "",
      summery: "",

      theme: "default",
      mdtheme: "",
      themes: ["default", "github", "vuepress"],
      mdthemes: ["light", "dark"],

      categorys: [],
      selectedCategory: null,

      cate: "",
      tags: null,

      Rtitle: "",
      Rcontent: "",
      RcategoryId: "",
      Rcate: "",
      Rtags: [],
      showModal: false,
      isLoggedIn: computed(() => store.getters.isLoggedIn),
      authorId: computed(() => store.getters.userId),
    });
    const store = useStore();
    const router = useRouter();
    const toast = useToast();
    state.categorys = store.getters.categorys;

    return {
      ...toRefs(state),
      toast,
      handleCreatePost: () => {
        state.tags =
          state.tags !== null ? state.tags.replace(/，/g, ",") : null;
        if (state.tags == null || state.tags == "") {
          state.Rtags = "标签不能为空";
          return;
        }
        axios
          .post(
            "/api/blog/",
            {
              title: state.title,
              content: state.content,
              category_id: state.selectedCategory
                ? state.selectedCategory.id
                : 0,
              summery: state.summery,
              tags: state.tags ? state.tags.split(",") : null,
              author: state.authorId,
            },
            {
              headers: {
                "content-type": "application/json",
                "X-CSRFTOKEN": Cookies.get("csrftoken"),
                Authorization: "Token " + state.isLoggedIn,
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
              state.RcategoryId = e.response.data.category_id
                ? e.response.data.category_id[0]
                : "";
              state.Rcontent = e.response.data.content
                ? e.response.data.content[0]
                : "";
              state.Rtitle = e.response.data.title
                ? e.response.data.title[0]
                : "";
              state.Rtags = e.response.data.tags ? e.response.data.tags[0] : "";
              if (e.response.data.detail) {
                toast.error(e.response.data.detail, { timeout: 2000 });
              }
            } else if (e.request) {
              console.log(e.request);
            } else {
              console.log(e.message);
            }
          });
      },
      changeTheme: (event) => {
        state.theme = event.target.value;
      },
      changeMDTheme: (event) => {
        state.mdtheme = event.target.value;
      },
      changeColor: (category) => {
        if (
          state.selectedCategory &&
          category.id === state.selectedCategory.id
        ) {
          return "border-red-400";
        }
        return "border-gray-300";
      },
      // 选取分类的方法
      chooseCategory: (category) => {
        // 如果点击已选取的分类，则将 selectedCategory 置空
        if (
          state.selectedCategory !== null &&
          state.selectedCategory.id === category.id
        ) {
          state.selectedCategory = null;
        }
        // 如果没选中当前分类，则选中它
        else {
          state.selectedCategory = category;
        }
      },
      toggleModal: () => {
        state.showModal = !state.showModal;
      },
      handleCreateCate: () => {
        axios
          .post(
            "/api/category/",
            {
              title: state.cate,
            },
            {
              headers: {
                "content-type": "application/json",
                "X-CSRFTOKEN": Cookies.get("csrftoken"),
                Authorization: "Token " + state.isLoggedIn,
              },
            }
          )
          .then((resp) => {
            if (resp.data.title) {
              toast.success("分类创建成功", { timeout: 2000 });
            }

            // 关闭modal
            state.showModal = !state.showModal;
          })
          .then(
            axios
              .get("/api/category/")
              .then((res) => {
                state.categorys = [];
                state.categorys.push(...res.data);
                store.dispatch("storeCategories", res.data);
              })
              .catch((error) => {
                console.log(error.message);
              })
          )
          .catch((e) => {
            if (e.response) {
              state.Rcate = e.response.data.title
                ? e.response.data.title[0]
                : "";
              if (state.Rcate) {
                toast.error(state.Rcate, { timeout: 2000 });
              }
              if (e.response.data.detail) {
                toast.error(e.response.data.detail, { timeout: 2000 });
              }
            } else if (e.request) {
              console.log(e.request);
            } else {
              console.log(e.message);
            }
          });
      },
      handleUploadImg: async (files, callback) => {
        //console.log(Array.from(files));
        const res = await Promise.all(
          Array.from(files).map((file) => {
            return new Promise((rev, rej) => {
              const form = new FormData();
              form.append("file", file);
              axios
                .post(`/api/blog/img/uploads/`, form, {
                  headers: {
                    "Content-Type": "multipart/form-data",
                    "X-CSRFTOKEN": Cookies.get("csrftoken"),
                    Authorization: "Token " + state.isLoggedIn,
                  },
                })
                .then((res) => rev(res))
                .catch((error) => rej(error));
            });
          })
        );

        callback(
          res.map((item) => {
            if (item.data.code === "0000") {
              toast.error("图片上传失败，请重试", { timeout: 2000 });
            }
            return item.data.url;
          })
        );
      },
    };
  },
};
</script>

<style>
code {
  color: #f66;
}
form {
  width: -webkit-fill-available;
}
</style>
