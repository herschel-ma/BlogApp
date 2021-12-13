<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="relative">
    <!-- Dropdown toggle button -->
    <button
      class="absolute right-0 flex items-center p-2 bg-gray-100 rounded-md w-44"
    >
      <span class="mr-4">Dropdown Menu</span>
      <svg
        class="w-5 h-5 text-gray-800 dark:text-white"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
          clip-rule="evenodd"
        />
      </svg>
    </button>
    <!-- Dropdown List -->
    <div
      class="absolute right-0 top-10 py-2 mt-2  bg-gray-100 divide-y divide-gray-600 rounded-md shadow-xl w-44"
    >
      <a
        href="#"
        class="block px-4 py-2 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
      >
        Dropdown List 1
      </a>
      <a
        href="#"
        class="block px-4 py-2 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
      >
        Dropdown List 2
      </a>
      <a
        href="#"
        class="block px-4 py-2 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
      >
        Dropdown List 3
      </a>
      <a
        href="#"
        class="block px-4 py-2 text-sm  text-gray-700 hover:bg-gray-400 hover:text-white"
      >
        Dropdown List 4
      </a>
    </div>
  </div>
</template>

<script>
export default {};
</script>
