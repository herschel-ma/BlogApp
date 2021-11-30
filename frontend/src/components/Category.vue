<template>
  <div class="px-8 mt-10">
    <h1 class="mb-4 text-xl font-bold text-gray-700">分类</h1>
    <div class="flex flex-col max-w-sm px-4 py-6 bg-white rounded-lg shadow-md">
      <ul>
        <li v-for="category in categories" :key="category">
          <a
            href="#"
            class="mx-1 font-bold text-gray-700 hover:text-gray-600 hover:underline"
          >
            - {{ category.title }}
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { onMounted, reactive, toRefs } from "vue";

export default {
  setup() {
    const state = reactive({
      categories: [],
    });
    onMounted(() => {
      axios
        .get("/api/category/")
        .then((res) => {
          state.categories.push(...res.data.results);
        })
        .catch((error) => {
          console.log(error.message.data);
        });
    });
    return {
      ...toRefs(state),
    };
  },
};
</script>
