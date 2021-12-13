<template>
  <div class="px-8">
    <h1 class="mb-4 text-xl font-bold text-gray-700">作者</h1>
    <div class="flex flex-col max-w-sm px-6 py-4 bg-white rounded-lg shadow-md">
      <ul class="-mx-4">
        <li class="flex items-center" v-for="user in authors" :key="user">
          <img
            :src="getAvatar(user)"
            alt="avatar"
            class="object-cover w-10 h-10
          mx-4 rounded-full"
          />
          <p>
            <a href="#" class="mx-1 font-bold text-gray-700 hover:underline">{{
              user.username
            }}</a>
            <span class="text-sm font-light text-gray-700">
              共有 {{ user.post_count }} 篇博文</span
            >
          </p>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { onMounted, reactive, toRefs } from "vue";
import { useStore } from "vuex";

export default {
  setup() {
    const state = reactive({
      authors: [],
    });
    const store = useStore();
    onMounted(() => {
      axios
        .get("/api/users/")
        .then((res) => {
          state.authors.push(...res.data);
          store.dispatch("storeUsers", res.data);
        })
        .catch((error) => {
          console.log(error.message.data);
        });
    });
    const getAvatar = (user) => {
      if (user.user !== null) {
        return user.user.avatar_url;
      } else if (user.avatar !== null) {
        return user.avatar.content;
      } else {
        return "https://img.paulzzh.com/touhou/random";
      }
    };
    return {
      ...toRefs(state),
      getAvatar,
    };
  },
};
</script>
