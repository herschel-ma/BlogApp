<template>
  <nav-bar />
  <router-view />
  <Footer />
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

<style>
body,
#app {
  background-color: rgb(236, 233, 233);
}
</style>
