<template>
  <div class="flex overflow-x-auto md:justify-center">
    <form
      class="flex flex-col justify-between md:mx-20 mx-2"
      method="PUT"
      @submit.prevent="handleCreate"
    >
      <label class="text-gray-600 font-light mt-5">标题:</label>
      <input
        type="text"
        placeholder="请修改标题"
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
            v-if="selectedCategory && cate.id == selectedCategory.id"
            class="relative inline-block border px-6 py-2 mb-2 rounded-md hover:border-red-300 border-red-300 text-base font-medium"
            :class="changeColor(cate)"
            @click.prevent="chooseCategory(cate)"
          >
            {{ cate.title }}
            <svg
              @click.stop.prevent="tolggleDeleteCate(cate)"
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 absolute -right-2 -top-2 
              bg-gray-400 text-red-50 rounded-full animate-pulse
              hover:text-red-500 hover:bg-red-300 transition delay-150"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
          <button
            v-else
            class="relative inline-block border px-6 py-2 mb-2 border-gray-300 rounded-md hover:border-red-300 text-base font-medium"
            :class="changeColor(cate)"
            @click.prevent="chooseCategory(cate)"
          >
            {{ cate.title
            }}<svg
              @click.stop.prevent="tolggleDeleteCate(cate)"
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 absolute -right-2 -top-2 bg-gray-400 text-red-50 rounded-full animate-pulse hover:text-red-500 hover:bg-red-300 transition delay-150"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
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
      <div
        class="md:grid md:grid-cols-5 md:gap-2 flex flex-wrap lg:flex lg:flex-wrap mb-2 item-center"
      >
        <span v-for="tag in tags" :key="tag.id" class="relative mr-2">
          <button
            v-if="checkTagExist(tag)"
            @click.prevent="chooseTag(tag)"
            class="inline-block border px-6 py-2 mb-2 rounded-md hover:border-red-300 border-red-300 text-base font-medium"
          >
            {{ tag.name }}
            <svg
              @click.stop.prevent="tolggleDeleteTag(tag)"
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 absolute -right-2 -top-2 bg-gray-400 text-red-50 rounded-full animate-pulse hover:text-red-500 hover:bg-red-300 transition delay-150"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </button>

          <button
            v-else
            @click.prevent="chooseTag(tag)"
            class="inline-block border px-6 py-2 mb-2 rounded-md hover:border-red-300 border-gray-300 text-base font-medium"
          >
            {{ tag.name }}
            <svg
              @click.stop.prevent="tolggleDeleteTag(tag)"
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 absolute -right-2 -top-2 bg-gray-400 text-red-50 rounded-full animate-pulse hover:text-red-500 hover:bg-red-300 transition delay-150"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
        </span>
        <span>
          <button
            class="bg-green-500 mb-2 text-white rounded-md px-6 py-2 text-base font-medium hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-300"
            id="open-btn"
            @click.prevent="toggleTagModal"
          >
            创建标签
          </button>
        </span>
      </div>
      <p v-show="Rtags" class="text-sm text-red-400 mb-2"></p>
      <label class="text-gray-600 font-light">摘要（非必须）:</label>
      <input
        type="text"
        placeholder="请修改摘要"
        class="lg:w-1/2 px-3 py-2 mb-3 border border-gray-300 rounded-lg text-gray-700 focus:outline-none focus:border-indigo-300"
        v-model="summery"
      />
      <label class="text-gray-600 font-light">内容:</label>

      <p v-show="Rcontent" class="text-sm text-red-400 mb-2">
        {{ Rcontent }}
      </p>
      <div class="flex flex-col">
        <select
          class="lg:w-1/2 mb-3 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          @change="changeMDTheme($event)"
        >
          <option v-for="t in mdthemes" :value="t" :key="t"
            >编辑器主题切换为 {{ t }}
          </option>
        </select>
        <select
          class="lg:w-1/2 mb-3 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
          @change="changeTheme($event)"
        >
          <option v-for="t in themes" :value="t" :key="t"
            >预览主题切换为 {{ t }}
          </option>
        </select>
      </div>

      <md-editor
        v-model="content"
        :preview-theme="theme"
        :theme="mdtheme"
        class="mb-5"
        :onSave="handleCreate"
        @onUploadImg="handleUploadImg"
      />

      <button
        type="submit"
        class="w-40 flex justify-center bg-indigo-500 text-gray-100 p-4 rounded-full tracking-wide font-semibold focus:outline-none focus:shadow-outline hover:bg-indigo-600 shadow-lg cursor-pointer transition ease-in duration-300"
      >
        更改并发布
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
                <span class="m-2  text-white" @click="showModal = false">
                  创建分类
                </span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </template>
  </ModalDialog>
  <ModalDialog :show="showDelModal" @close="showDelModal = false">
    <template v-slot:innerForm>
      <div
        class="xs:w-4/5 sm:w-3/4 md:w-1/2 h-1/3 flex flex-col bg-white 
        bg-opacity-90 space-y-8 justify-center align-middle z-10"
      >
        <div class="p-3 z-10 text-center text-3xl">确定要删除吗？</div>
        <div class="container flex justify-center align-middle space-x-5">
          <div
            @click="showDelModal = false"
            class="rounded-lg shawdow-lg cursor-pointer bg-green-600 z-10 p-3"
          >
            不，我不删除了
          </div>
          <div
            @click="deleteTag"
            class="rounded-lg shawdow-lg cursor-pointer bg-red-600 z-10 p-3"
          >
            是的,我确定
          </div>
        </div>
      </div>
    </template>
  </ModalDialog>
  <ModalDialog :show="showDelCateModal" @close="showDelCateModal = false">
    <template v-slot:innerForm>
      <div
        class="xs:w-4/5 sm:w-3/4 md:w-1/2 h-1/3 flex flex-col bg-white 
        bg-opacity-90 space-y-8 justify-center align-middle z-10"
      >
        <div class="p-3 z-10 text-center text-3xl">确定要删除吗？</div>
        <div class="container flex justify-center align-middle space-x-5">
          <div
            @click="showDelCateModal = false"
            class="rounded-lg shawdow-lg cursor-pointer bg-green-600 z-10 p-3"
          >
            不，我不删除了
          </div>
          <div
            @click="deleteCate"
            class="rounded-lg shawdow-lg cursor-pointer bg-red-600 z-10 p-3"
          >
            是的,我确定
          </div>
        </div>
      </div>
    </template>
  </ModalDialog>
  <ModalDialog :show="showTagModal" @close="showTagModal = false">
    <template v-slot:innerForm>
      <div
        class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto"
      >
        <div class="modal-content py-4 text-left px-6">
          <div class="flex justify-center items-center pb-3">
            <p class="text-2xl font-bold text-center">创建标签</p>
          </div>

          <form
            class="mt-6"
            method="POST"
            @submit.prevent="handleCreateTag($event)"
          >
            <div>
              <label
                for="tag"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >标签名：</label
              >
              <input
                type="text"
                v-model="tagTitle"
                id="tag"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <label
                for="tagSlug"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >标签唯一标识：</label
              >
              <input
                type="text"
                v-model="tagSlug"
                id="tagSlug"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
            </div>

            <div class="mt-6">
              <button
                type="submit"
                class="flex items-center justify-center w-full px-6 py-2 text-sm font-medium text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:bg-blue-400 focus:outline-none"
              >
                <span class="m-2  text-white" @click="showTagModal = false">
                  创建标签
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
import { onMounted, reactive, toRefs, computed, watch } from "vue";
import axios from "axios";
import Cookies from "js-cookie";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import MdEditor from "md-editor-v3";
import "md-editor-v3/lib/style.css";
import ModalDialog from "@/components/ModalDialog";
import pinyin from "@/utils/utils";

export default {
  props: {
    slug: {
      type: String,
      required: true,
    },
    author: {
      type: String,
      required: true,
    },
  },
  components: {
    MdEditor,
    ModalDialog,
  },
  setup(props) {
    const toast = useToast();
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
      Rtitle: "",
      Rcontent: "",
      RcategoryId: "",
      showModal: false,
      showDelModal: false,
      showDelCateModal: false,
      showTagModal: false,
      cate: "",
      Rcate: "",
      isLoggedIn: computed(() => store.getters.isLoggedIn),
      delTag: computed(() => store.getters.delTag),
      delCate: computed(() => store.getters.delCate),
      tags: [],
      Rtags: "",
      tagTitle: "",
      RtagTitle: "",
      tagSlug: "",
      RtagSlug: "",
      selectedTag: [],
      authorId: computed(() => store.getters.userId),
    });
    watch(
      () => state.tagTitle,
      (tagTitle, prevTagTitle) => {
        if (tagTitle !== "" && tagTitle !== prevTagTitle) {
          state.tagSlug = pinyin.isSupported()
            ? pinyin.convertToPinyin(state.tagTitle, "-", true)
            : "对不住，换个浏览器试试吧";
        }
      }
    );

    const store = useStore();
    const router = useRouter();
    // 默认渲染的所有标签
    state.tags = store.getters.tags;
    state.categorys = store.getters.categorys;
    onMounted(() => {
      axios
        .get(`/api/blog/${props.slug}/`, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: state.isLoggedIn,
          },
        })
        .then((res) => {
          state.title = res.data.title;
          state.content = res.data.content;
          state.summery = res.data.summery;
          state.selectedCategory = res.data.category;
          state.selectedTag = res.data.tags;
        })
        .catch((error) => {
          console.log(error.message);
        });
    });
    return {
      ...toRefs(state),
      toast,
      checkTagExist: (tag) => {
        // console.log(tag);
        // console.log(state.selectedTag);
        if (state.selectedTag && state.selectedTag.length > 0) {
          if (state.selectedTag.indexOf(tag.name) !== -1) {
            return true;
          }
        }
        return false;
      },
      tolggleDeleteTag: (tag) => {
        // 存储要删除的tag的id,删除后需要删除存储id并跳转页面
        store.dispatch("storeDelTag", tag.id);
        state.showDelModal = !state.showDelModal;
      },
      deleteTag: () => {
        axios
          .delete(`/api/tag/${state.delTag}`, {
            headers: {
              "Content-Type": "Application/json",
              "X-CSRFTOKEN": Cookies.get("csrftoken"),
              Authorization: state.isLoggedIn,
            },
          })
          .then(() => {
            toast.success("删除标签成功", { timeout: 2000 });
            store.dispatch("deleteDeleteTag");
            state.showDelModal = !state.showDelModal;
            //router.push({ name: "home" });
          })
          .catch((e) => {
            console.log(e);
          });
        setTimeout(() => {
          axios
            .get("/api/tag/")
            .then((res) => {
              state.tags = [];
              state.tags.push(...res.data);
              store.dispatch("storeTags", res.data);
            })
            .catch((error) => {
              console.log(error.message);
            });
        }, 500);
      },
      tolggleDeleteCate: (cate) => {
        // 存储要删除的分类的id,删除后需要删除存储id并跳转页面
        store.dispatch("storeDelCata", cate.id);
        state.showDelCateModal = !state.showDelCateModal;
      },
      deleteCate: () => {
        axios
          .delete(`/api/category/${state.delCate}`, {
            headers: {
              "Content-Type": "Application/json",
              "X-CSRFTOKEN": Cookies.get("csrftoken"),
              Authorization: state.isLoggedIn,
            },
          })
          .then(() => {
            toast.success(`删除分类成功`, { timeout: 2000 });
            store.dispatch("deleteDeleteCata");
            state.showDelCateModal = !state.showDelCateModal;
          })
          .catch((e) => {
            console.log(e);
          });
        setTimeout(() => {
          axios
            .get("/api/category/")
            .then((res) => {
              state.categorys = [];
              state.categorys.push(...res.data);
              store.dispatch("storeCategories", res.data);
            })
            .catch((error) => {
              console.log(error.message);
            });
        }, 500);
      },
      handleCreate: () => {
        axios
          .put(
            `/api/blog/${props.slug}/`,
            {
              title: state.title,
              content: state.content,
              summery: state.summery,
              category_id: state.selectedCategory
                ? state.selectedCategory.id
                : 0,
              // 提交的标签
              tags: state.selectedTag,
              author: state.authorId,
            },
            {
              headers: {
                "Content-Type": "Application/json",
                "X-CSRFTOKEN": Cookies.get("csrftoken"),
                Authorization: state.isLoggedIn,
              },
            }
          )
          .then((resp) => {
            if (resp.data.title) {
              toast.success("已经成功修改", {
                timeout: 2000,
              });
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
      chooseTag: (tag) => {
        // 如果选择的标签不在提交的标签里，则添加, 否则删除
        // console.log(tag);
        // console.log(state.selectedTag);
        if (state.selectedTag.length > 0) {
          const index = state.selectedTag.indexOf(tag.name);
          if (index > -1) {
            // 删除存在的元素
            state.selectedTag.splice(index, 1);
            return;
          } else {
            // 赋值给提交的标签
            state.selectedTag.push(tag.name);
            return;
          }
        } else if (state.selectedTag.length === 0) {
          state.selectedTag.push(tag.name);
        }
      },
      // 改变样式

      toggleModal: () => {
        state.showModal = !state.showModal;
      },
      toggleTagModal: () => {
        state.showTagModal = !state.showTagModal;
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
            // 刷新分类
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
      handleCreateTag: (event) => {
        event.preventDefault();
        axios
          .post(
            "/api/tag/",
            {
              name: state.tagTitle,
              slug: state.tagSlug,
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
            if (resp.data.name) {
              toast.success(`标签${resp.data.name}创建成功`, { timeout: 2000 });
            }
            // 关闭modal
            state.showTagModal = !state.showTagModal;
          })
          .catch((e) => {
            if (e.response) {
              state.RtagTitle = e.response.data.name
                ? e.response.data.name[0]
                : "";
              state.RtagSlug = e.response.data.slug
                ? e.response.data.slug[0]
                : "";
              if (state.RtagTitle) {
                toast.error("标签, " + state.RtagTitle, { timeout: 2000 });
              }
              if (state.RtagSlug) {
                toast.error("标签唯一标识, " + state.RtagSlug, {
                  timeout: 2000,
                });
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
        setTimeout(() => {
          axios
            .get("/api/tag/")
            .then((res) => {
              state.tags = [];
              state.tags.push(...res.data);
              store.dispatch("storeTags", res.data);
            })
            .catch((error) => {
              console.log(error.message);
            });
        }, 500);
      },
      handleUploadImg: async (files, callback) => {
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
