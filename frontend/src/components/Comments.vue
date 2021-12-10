<template>
  <br /><br />
  <h3 id="comment-form">发表评论</h3>
  <textarea
    v-model="message"
    :placeholder="placeholder"
    name="comment"
    id="comment-area"
    cols="60"
    rows="10"
  ></textarea>
  <div>
    <button @click="submit" class="h-9 w-20 bg-blue-400">发布</button>
  </div>
  <br />
  <p>已有 {{ comments.length }} 条评论</p>
  <hr />

  <div v-if="comments.length > 0">
    <div class="bg-gray-100 flex justify-center items-center">
      <div
        class="bg-white w-full sm:max-w-7xl h-auto shadow px-3 py-4 flex flex-col space-y-2"
      >
        <div
          v-for="comment in comments"
          :key="comment.id"
          class="flex items-center space-x-2"
        >
          <div
            class="group relative flex flex-shrink-0 self-start cursor-pointer"
          >
            <img
              :src="getAvatar(comment)"
              alt="头像"
              class="h-8 w-8 object-fill rounded-full"
            />
          </div>

          <div class="flex items-center justify-center space-x-2">
            <div class="block">
              <div class="flex items-center space-x-2">
                <div class="bg-gray-100 w-auto rounded-xl px-2 pb-2">
                  <div class="font-medium">
                    <div class="text-sm">
                      <small :id="getCommentId(comment)">{{
                        comment.author.username
                      }}</small>
                      <span v-if="comment.parent">
                        <small> 对 </small>
                        <span class="parent">
                          <a :href="getAnchor(comment)"
                            ><small>{{
                              comment.parent.author.username
                            }}</small></a
                          >
                        </span>
                      </span>
                      <small> 说道：</small>
                    </div>
                  </div>
                  <div class="text-xs">
                    {{ comment.content }}
                  </div>
                  <div v-if="comment.parent" class="ml-2 text-xs bg-blue-200">
                    <a :href="getAnchor(comment)">
                      {{ comment.parent.content }}
                    </a>
                  </div>
                </div>
                <div
                  class="self-stretch flex justify-center items-center transform transition-opacity duration-200 opacity-0 hover:opacity-100"
                >
                  <a href="#comment-form" @click="clearReplyTo">
                    <div
                      class="text-xs cursor-pointer flex h-6 w-6 transform transition-colors duration-200 hover:bg-gray-100 rounded-full items-center justify-center"
                    >
                      <svg
                        class="w-4 h-6"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"
                        ></path>
                      </svg>
                    </div>
                  </a>
                </div>
              </div>
              <div class="flex justify-start items-center text-xs w-full">
                <div
                  class="font-semibold text-gray-700 px-2 flex items-center justify-center space-x-1"
                >
                  <a class="hover:underline">
                    <button class="commentBtn" @click="replyTo(comment)">
                      <a href="#comment-form">
                        <small>回复</small>
                      </a>
                    </button>
                  </a>
                  <small class="self-center">.</small>
                  <a class="hover:underline">
                    <small>{{ comment.created_time }}</small>
                  </a>
                </div>
              </div>

              <!-- New Subcomment Paste Here !! -->
            </div>
          </div>
        </div>
        <!-- New Comment Paste Here -->
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Cookies from "js-cookie";
import { toRefs, reactive, watch, computed } from "vue";
import { useStore } from "vuex";
import { useToast } from "vue-toastification";
export default {
  props: {
    article: {
      type: Object,
    },
  },
  setup(props) {
    const store = useStore();
    const toast = useToast();
    const state = reactive({
      comments: [],
      message: "",
      placeholder: "说呗...",
      parentId: null,
      isLoggedIn: computed(() => store.getters.isLoggedIn),
    });
    watch(
      () => props.article,
      (article) => {
        state.comments = article !== null ? article.comments : [];
      }
    );
    const submit = () => {
      axios
        .post(
          "/api/comments/",
          {
            content: state.message,
            article_id: props.article.id,
            parent_id: state.parentId || null,
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
          // 将评论添加到顶部
          state.comments.unshift(response.data);
          state.message = "";
          toast.success("留言成功", { timeout: 2000 });
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const replyTo = (comment) => {
      state.parentId = comment.id;
      state.placeholder = "对" + comment.author.username + "说：";
    };
    const clearReplyTo = () => {
      state.parentId = null;
      state.placeholder = "说呗...";
    };
    const getCommentId = (comment) => {
      return `comment-${comment.id}`;
    };
    const getAnchor = (comment) => {
      if (comment.parent) return `#comment-${comment.parent.id}`;
    };
    const getAvatar = (comment) => {
      if (comment.author.user) {
        return comment.author.user.avatar_url;
      }
      return "https://img.paulzzh.com/touhou/random";
    };
    return {
      ...toRefs(state),
      submit,
      replyTo,
      clearReplyTo,
      getCommentId,
      getAnchor,
      getAvatar,
    };
  },
};
</script>
