<template>
  <div class="container my-12 mx-auto px-4 md:px-12">
    <div class="flex flex-wrap -mx-1 lg:-mx-4 space-y-4">
      <div class="flex flex-row">
        <!--Category-->
        <div class="flex flex-wrap space-x-3">
          <!-- Title -->
          <div class="flex space-x-2">
            <div
              v-for="cate in linksCategorys"
              :key="cate.id"
              class="p-2 ml-6 bg-pink-500 cursor-pointer"
              @click="getLinks(cate.id)"
            >
              {{ cate.title }}
            </div>
            <button
              class="btn btn-primary bg-purple-400 p-2"
              @click="toggleModal"
            >
              添加分类
            </button>
            <button
              class="btn btn-primary bg-purple-400 p-2"
              @click="toggleLinkModal"
            >
              申请友链
            </button>
          </div>
          <!--End Title -->
          <!-- Link -->
          <div class="flex flex-wrap space-x-2">
            <!-- Column -->
            <div
              v-for="link in links"
              :key="link.id"
              class="my-1 px-1 w-full md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3"
            >
              <!-- Article -->
              <article class="overflow-hidden rounded-lg shadow-lg">
                <a :href="link.link_url">
                  <img
                    alt="Placeholder"
                    class="block h-auto w-full"
                    :src="
                      link.thumbnail_url
                        ? link.thumbnail_url
                        : 'https://picsum.photos/600/400/?random'
                    "
                  />
                </a>

                <header class="flex justify-between p-2 md:p-4">
                  <h1 class="text-base">
                    <a
                      class="no-underline hover:underline text-black"
                      :href="link.link_url"
                    >
                      {{ link.description }}
                    </a>
                  </h1>
                  <p class="text-grey-darker text-sm">
                    {{ link.created_time }}
                  </p>
                </header>

                <footer
                  class="flex items-center justify-between leading-none p-2 md:p-4"
                >
                  <a
                    class="flex items-center no-underline hover:underline text-black"
                    :href="link.link_url"
                  >
                    <img
                      alt="Placeholder"
                      class="block rounded-full"
                      src="https://picsum.photos/32/32/?random"
                    />
                    <p class="ml-2 text-sm">
                      {{ link.title }}
                    </p>
                  </a>
                  <p class="ml-2 text-sm">
                    {{ link.category }}
                  </p>
                </footer>
              </article>
              <!-- END Article -->
            </div>
            <!--End Column -->
          </div>
          <!-- END Link -->
        </div>
        <!--END Category -->
      </div>
    </div>
  </div>
  <!--创建链接分类-->
  <ModalDialog :show="showModal" @close="showModal = false">
    <template v-slot:innerForm>
      <div
        class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto"
      >
        <div class="modal-content py-4 text-left px-6">
          <div class="flex justify-center items-center pb-3">
            <p class="text-2xl font-bold text-center">创建分类</p>
          </div>

          <form
            class="mt-6"
            method="POST"
            @submit.prevent="handleCreateCate($event)"
          >
            <div>
              <label
                for="cate"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >分类名：</label
              >
              <input
                type="text"
                v-model="cate"
                id="tag"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
            </div>

            <div class="mt-6">
              <button
                type="submit"
                class="flex items-center justify-center w-full px-6 py-2 text-sm font-medium text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:bg-blue-400 focus:outline-none"
              >
                <span
                  class="m-2  text-white"
                  @click.prevent="showModal = false"
                >
                  创建分类
                </span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </template>
  </ModalDialog>
  <!--申请友链-->
  <ModalDialog :show="showLinkModal" @close="showLinkModal = false">
    <template v-slot:innerForm>
      <div
        class="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto"
      >
        <div class="modal-content py-4 text-left px-6">
          <div class="flex justify-center items-center pb-3">
            <p class="text-2xl font-bold text-center">申请友链</p>
          </div>
          <form method="POST">
            <label
              for="thumbnail"
              class="block text-sm text-gray-800 dark:text-gray-200"
              >上传封面</label
            >
            <input
              type="file"
              id="thumbnail"
              @change="onFileChange"
              class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
            />
            <p v-show="Rthumbnail_url" class="text-sm text-red-400">
              {{ Rthumbnail_url }}
            </p>
          </form>

          <form
            class="mt-6"
            method="POST"
            @submit.prevent="handleCreateLink($event)"
          >
            <div>
              <label
                for="title"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >标题</label
              >
              <input
                type="text"
                v-model="title"
                id="title"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <p v-show="Rtitle" class="text-sm text-red-400">{{ Rtitle }}</p>
              <label
                for="description"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >描述</label
              >
              <input
                type="text"
                v-model="description"
                id="description"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <p v-show="Rdescription" class="text-sm text-red-400">
                {{ Rdescription }}
              </p>
              <input
                type="hidden"
                id="thumbnail_url"
                v-model="thumbnail_url"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <label
                for="link_url"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >链接</label
              >
              <input
                type="text"
                id="link_url"
                v-model="link_url"
                class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"
              />
              <p v-show="Rlink_url" class="text-sm text-red-400">
                {{ Rlink_url }}
              </p>
              <label
                for="link_url"
                class="block text-sm text-gray-800 dark:text-gray-200"
                >分类</label
              >
              <select
                id="category"
                v-model="cateSelected"
                @change="getCateSelected"
              >
                <option
                  v-for="cate in linksCategorys"
                  :key="cate.id"
                  :value="cate.id"
                >
                  {{ cate.title }}
                </option>
              </select>
              <p v-show="Rcategory" class="text-sm text-red-400">
                {{ Rcategory }}
              </p>
            </div>

            <div class="mt-6">
              <button
                type="submit"
                class="flex items-center justify-center w-full px-6 py-2 text-sm font-medium text-white transition-colors duration-200 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:bg-blue-400 focus:outline-none"
              >
                <span
                  class="m-2  text-white"
                  @click.prevent="showLinkModal = false"
                >
                  申请
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
import { onMounted, reactive, toRefs, computed } from "vue";
import axios from "axios";
import Cookies from "js-cookie";
import { useStore } from "vuex";
import ModalDialog from "@/components/ModalDialog";
import { useToast } from "vue-toastification";

export default {
  components: {
    ModalDialog,
  },
  setup() {
    const store = useStore();
    const toast = useToast();
    const state = reactive({
      links: Array,
      linksCategorys: [],
      cate: "",
      Rcate: "",
      showModal: false,
      showLinkModal: false,
      isLoggedIn: computed(() => store.getters.isLoggedIn),
      title: "",
      description: "",
      thumbnail_url: "",
      link_url: "",
      cateSelected: 1,
      Rcategory: "",
      Rtitle: "",
      Rdescription: "",
      Rthumbnail_url: "",
      Rlink_url: "",
    });

    const handleCreateCate = () => {
      axios
        .post(
          "/api/linksCategory/",
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
        .then(() => {
          getLinkCategorys();
        })
        .catch((e) => {
          if (e.response) {
            state.Rtitle = e.response.data.title
              ? e.response.data.title[0]
              : "";
            if (state.Rtitle) {
              toast.error(state.Rtitle, { timeout: 2000 });
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
    };
    const getLinkCategorys = () => {
      axios
        .get(`/api/linksCategory/`, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          state.linksCategorys = res.data;
        })
        .catch((error) => console.log(error));
    };
    const getLinks = (category) => {
      const url =
        category !== 0
          ? `/api/links/?category=${category}&show=True`
          : `/api/links/?show=True`;
      axios
        .get(url, {
          headers: {
            "Content-Type": "Application/json",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          state.links = [];
          state.links.push(
            ...res.data.map((a) => {
              a.created_time = new Date(a.created_time).toLocaleDateString(
                "zh-hans"
              );
              return a;
            })
          );
          return res.data;
        })
        .catch((error) => console.log(error));
    };
    const onFileChange = (e) => {
      const file = e.target.files[0];
      let formData = new FormData();
      formData.append("content", file);
      axios
        .post(`/api/linsThumbnailUpload/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFTOKEN": Cookies.get("csrftoken"),
            Authorization: "Token " + state.isLoggedIn,
          },
        })
        .then((res) => {
          state.thumbnail_url = res.data.content;
          toast.success("上传封面成功", { timeout: 2000 });
          console.log(res.data);
        })
        .catch((error) => console.log(error));
    };
    const handleCreateLink = () => {
      axios
        .post(
          `/api/links/`,
          {
            title: state.title,
            description: state.description,
            thumbnail_url: state.thumbnail_url,
            link_url: state.link_url,
            category: state.cateSelected,
          },
          {
            headers: {
              "X-CSRFTOKEN": Cookies.get("csrftoken"),
              Authorization: "Token " + state.isLoggedIn,
            },
          }
        )
        .then(() => {
          toast.success("友链申请成功！", { timeout: 2000 });
          state.showLinkModal = false;
        })
        .catch((e) => {
          if (e.response) {
            state.Rtitle = e.response.data.title
              ? e.response.data.title[0]
              : "";
            state.Rdescription = e.response.data.description
              ? e.response.data.description[0]
              : "";
            state.Rlink_url = e.response.data.link_url
              ? e.response.data.link_url[0]
              : "";
            state.Rthumbnail_url = e.response.data.thumbnail_url
              ? e.response.data.thumbnail_url[0]
              : "";
            state.Rcategory = e.response.data.category
              ? e.response.data.category[0]
              : "";
            if (e.response.data.detail) {
              toast.error(e.response.data.detail, { timeout: 2000 });
            }
          } else if (e.request) {
            console.log(e.request);
          } else {
            console.log(e.message);
          }
        });
    };
    const toggleModal = () => {
      state.showModal = !state.showModal;
    };
    const toggleLinkModal = () => {
      state.showLinkModal = !state.showLinkModal;
    };
    onMounted(() => {
      getLinkCategorys();
      getLinks(1);
    });
    return {
      ...toRefs(state),
      handleCreateCate,
      toggleModal,
      toggleLinkModal,
      getLinks,
      onFileChange,
      handleCreateLink,
    };
  },
};
</script>
