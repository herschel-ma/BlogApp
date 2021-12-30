<template>
  <div style="overscroll-behavior: none;" class="w-full h-5/6 bg-gray-200">
    <div
      class="fixed w-full bg-green-400 h-16 pt-2 text-white flex justify-between shadow-md z-10"
      style="top:0px; overscroll-behavior: none;"
    >
      <!-- back button -->
      <router-link to="/">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          class="w-12 h-12 my-1 text-green-100 ml-2"
        >
          <path
            class="text-green-100 fill-current"
            d="M9.41 11H17a1 1 0 0 1 0 2H9.41l2.3 2.3a1 1 0 1 1-1.42 1.4l-4-4a1 1 0 0 1 0-1.4l4-4a1 1 0 0 1 1.42 1.4L9.4 11z"
          />
        </svg>
      </router-link>
      <div class="my-3 text-green-100 font-bold text-lg tracking-wide">
        聊天室
      </div>
      <!-- 3 dots -->
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        class="icon-dots-vertical w-8 h-8 mt-2 mr-2"
      >
        <path
          class="text-green-100 fill-current"
          fill-rule="evenodd"
          d="M12 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"
        />
      </svg>
    </div>

    <div class="w-full h-full">
      <div class="clearfix" v-for="(message, index) in messages" :key="index">
        <div
          :class="getposition(message)"
          class="w-3/4 mx-4 my-2 p-4 rounded-lg relative"
        >
          <span class="text-sm border-r-4 border-red-500 pr-2">
            {{ message.sender }}
          </span>
          <span
            class="messages pl-2
            "
          >
            {{ message.message }}
          </span>
          <div class="text-xs absolute -bottom-3 right-1 p-2 mb-1">
            {{ message.sendtime }}
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="w-full flex justify-between bg-green-100">
    <textarea
      id="chat-message-input"
      class="flex-grow m-2 py-2 px-4 mr-1 rounded-full border border-gray-300 bg-gray-200 resize-none"
      rows="1"
      placeholder="Message..."
      v-model="message_sent"
      @keyup.enter="sendMessage"
      style="outline: none;"
    ></textarea>
    <button class="m-2" @click.prevent="sendMessage" style="outline: none;">
      <svg
        class="svg-inline--fa text-green-400 fa-paper-plane fa-w-16 w-12 h-12 py-2 mr-2"
        aria-hidden="true"
        focusable="false"
        data-prefix="fas"
        data-icon="paper-plane"
        role="img"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 512 512"
      >
        <path
          fill="currentColor"
          d="M476 3.2L12.5 270.6c-18.1 10.4-15.8 35.6 2.2 43.2L121 358.4l287.3-253.2c5.5-4.9 13.3 2.6 8.6 8.3L176 407v80.5c0 23.6 28.5 32.9 42.5 15.8L282 426l124.6 52.2c14.2 6 30.4-2.9 33-18.2l72-432C515 7.8 493.3-6.8 476 3.2z"
        />
      </svg>
    </button>
  </div>
</template>

<script>
import { onMounted, reactive, toRefs, computed } from "vue";
import { useStore } from "vuex";
export default {
  setup() {
    const store = useStore();
    const state = reactive({
      messages: [],
      message_sent: "",
      websocket: null,
      roomId: 1,
      sender: computed(() => store.getters.username),
    });
    const sendMessage = () => {
      state.websocket.send(
        JSON.stringify({
          message: state.message_sent,
        })
      );
      state.message_sent = "";
    };
    const getposition = (message) => {
      if (state.sender !== message.sender) return "float-left bg-gray-300";
      return "float-right bg-green-300";
    };
    onMounted(() => {
      const chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/" + state.roomId + "/"
      );

      chatSocket.onmessage = function(e) {
        state.messages.push(JSON.parse(e.data));
      };

      chatSocket.onclose = function() {
        console.error("Chat socket closed unexpectedly");
      };

      document.querySelector("#chat-message-input").focus();
      state.websocket = chatSocket;
    });
    return {
      ...toRefs(state),
      sendMessage,
      getposition,
    };
  },
};
</script>
<style>
.messages {
  /*父元素设置为flex后，子元素会自动布局并适应宽度，
  但里面的文本文字超出边界却无法换 */
  overflow-wrap: break-word;
}
</style>
