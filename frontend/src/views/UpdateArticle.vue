<template>
  <form
    class="flex flex-col justify-between ml-5"
    method="PUT"
    @submit.prevent="handleCreate"
  >
    <label class="text-gray-600 font-light">Title:</label>
    <input
      type="text"
      placeholder="{{title}}"
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
import { onMounted, reactive, toRefs } from "vue";
import axios from "axios";
import Cookies from "js-cookie";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import MdEditor from "md-editor-v3";
import "md-editor-v3/lib/style.css";

export default {
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  components: {
    MdEditor,
  },
  setup(props) {
    const toast = useToast();
    const state = reactive({
      title: "",
      content: "",
      theme: "default",
    });
    const store = useStore();
    const router = useRouter();

    onMounted(() => {
      axios
        .get(`/api/blog/${props.slug}/`)
        .then((res) => {
          state.title = res.data.title;
          state.content = res.data.content;
        })
        .catch((error) => {
          console.log(error.message);
        });
    });
    return {
      ...toRefs(state),
      toast,
      handleCreate: () => {
        axios
          .put(
            `/api/blog/${props.slug}/`,
            {
              title: state.title,
              content: state.content,
            },
            {
              headers: {
                "Content-Type": "Application/json",
                "X-CSRFTOKEN": Cookies.get("csrftoken"),
                Authorization: store.state.isLoggedIn,
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
              if (e.response.data.detail) {
                toast.error(e.response.data.detail, {
                  timeout: 3000,
                });
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
