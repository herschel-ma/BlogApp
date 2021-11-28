<template>
  <nav-bar />
  <router-view />
  <Footer class="mt-10" />
</template>

<script>
import NavBar from "@/components/Navbar.vue";
import Footer from "@/components/Footer";

export default {
  name: "App",
  components: {
    NavBar,
    Footer,
  },
};
</script>

<style></style>
