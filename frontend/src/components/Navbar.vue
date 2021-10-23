 <template>
  <!-- navbar goes here -->
  <nav class="bg-gray-100">
    <div class="max-w-7xl mx-auto px-2">
      <div class="flex justify-between">
        <div class="flex space-x-3">
          <!-- logo -->
          <div>
            <a href="#" class="flex items-center py-5 px-3 text-gray-600 hover:text-black">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mr-2 text-red-400 hover:text-red-500"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z"
                  clip-rule="evenodd"
                />
              </svg>
              <router-link to="/" class="font-bold">Home</router-link>
            </a>
          </div>
          <!-- primary nav -->
          <div class="hidden md:flex space-x-5 items-center">
            <a href="#" class="py-5 px-2 text-gray-700 hover:text-black">Blog</a>
            <a href="#" class="text-gray-700 hover:text-black">Projects</a>
          </div>
        </div>
        <!-- secordary nav -->
        <div class="hidden md:flex space-x-2 items-center mr-3">
          <a href="/auth/login/" class="py-5 px-4">Login</a>
          <a
            href="/rest-auth/registration/"
            class="py-2 px-3 bg-yellow-400 hover:bg-yellow-300 text-yellow-700 hover:text-yellow-800 rounded transition duration-100"
          >Signup</a>
        </div>
        <!-- mobile button goes here -->
        <div class="md:hidden flex items-center">
          <button @click="showMobileMenu">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </button>
        </div>
      </div>
      <!-- mobile menu -->
      <div :class="showMenu" class="hidden" ref="menu">
        <router-link to="/post" class="block py-2 px-4 text-sm hover:bg-gray-200">Blog</router-link>
        <router-link to="/post" class="block py-2 px-4 text-sm hover:bg-gray-200">Projects</router-link>
        <router-link to="/post" class="block py-2 px-4 text-sm hover:bg-gray-200">Friendly Link</router-link>
      </div>
    </div>
  </nav>
  <!--content goes here-->
</template> 

<script>
export default {
  name: "Navbar",
  data() {
    return {
    }
  },
  methods: {
    showMobileMenu() {
      this.$refs.menu.classList.toggle('hidden')
    }
  },
}
</script>

