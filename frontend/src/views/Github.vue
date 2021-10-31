<template>
<div class="flex flex-col items-center mt-10">
  <p class="mb-10">
    github 登陆中 ...
  </p>
  <div 
    style="border-top-color: transparent"
    class="w-16 h-16 border-4 border-red-400 border-double rounded-full animate-spin"></div>
</div>
</template>

<script>

import { onMounted } from "vue"
export default {
  setup() {
    onMounted(() => {
      window.location.href = "https://github.com/login/oauth/authorize?client_id=cbcfe78fa71816693cd2"
    })
  } 
}
</script>
