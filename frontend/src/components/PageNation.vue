<template>
  <!--pagenation-->
  <div class="mt-8">
    <div class="flex">
      <a
        href
        @click.prevent="clickPrevious"
        class="px-3 py-2 mx-1 font-medium text-gray-500 bg-white rounded-md cursor-not-allowed"
      >previous</a>

      <a
        v-for="i in results"
        :key="i"
        class="px-3 py-2 mx-1 font-medium text-gray-700 bg-white rounded-md hover:bg-blue-500 hover:text-white"
        href
      >{{ i }}</a>
      <a
        href
        @click.prevent="clickNext"
        class="px-3 py-2 mx-1 font-medium text-gray-700 bg-white rounded-md hover:bg-blue-500 hover:text-white"
      >Next</a>
    </div>
  </div>
</template>
<script>
export default {
  emits: ['clickNext', 'clickPrevious', 'clickNumber'],
  props: {
    results: {
      type: Number,
      required: true
    }
  },
  setup(props, { emit }) {
    const methods = {
      clickPrevious: () => emit('clickPagenation', 'previous'),
      clickNext: () => emit('clickPagenation', 'next'),
      clickNumber: () => emit('clickPagenation', 'number'),
    }
    return { ...methods, }
  }
}
</script>
