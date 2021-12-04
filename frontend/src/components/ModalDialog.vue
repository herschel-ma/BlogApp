<template>
  <div
    v-if="show"
    class="modal fixed w-full h-full top-0 left-0 flex items-center justify-center"
  >
    <div
      @click.self="close_modal()"
      class="modal-overlay absolute w-full h-full bg-gray-900 opacity-50"
    ></div>

    <slot name="innerForm"></slot>
  </div>
</template>

<script>
import { reactive, toRefs } from "vue";
export default {
  name: "ModalDialog",
  emits: ["close"],
  props: {
    show: Boolean,
  },
  setup(props, { emit }) {
    const state = reactive({
      firstname: "",
      lastname: "",
      gender: "",
      residence: "",
      show: props.show,
    });
    return {
      ...toRefs(state),
      close_modal() {
        emit("close");
      },
    };
  },
};
</script>
