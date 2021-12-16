<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="h-auto flex flex-col justify-content align-middle">
    <div class="flex flex-col">
      <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
          <div class="overflow-hidden">
            <table class="min-w-full text-center">
              <thead class="border-b">
                <tr>
                  <th
                    scope="col"
                    class="text-sm font-medium text-gray-900 px-6 py-4"
                  >
                    时间
                  </th>
                  <th
                    scope="col"
                    class="text-sm font-medium text-gray-900 px-6 py-4"
                  >
                    事件
                  </th>
                  <th
                    scope="col"
                    class="text-sm font-medium text-gray-900 px-6 py-4"
                  >
                    标题
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="(info, index) in infos"
                  :key="index"
                  class="border-b"
                  :class="getColor(info)"
                >
                  <td
                    class="text-sm text-gray-900 font-medium px-6 py-4 whitespace-nowrap"
                  >
                    {{ info.year }}
                  </td>
                  <td
                    class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                  >
                    {{ info.type }}
                  </td>
                  <td
                    class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                  >
                    <a :href="info.link"> {{ info.title }}</a>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { reactive, toRefs, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";
export default {
  setup() {
    const toast = useToast();
    const router = useRouter();
    const state = reactive({
      url: "https://query.asilu.com/today/list/",
      infos: [],
    });
    const getHistoryToadayInfo = () => {
      axios
        .get(state.url, {
          headers: {
            "Content-Type": "Application/json",
          },
        })
        .then((res) => {
          if (res.data.code === 200) {
            state.infos = res.data.data;
          }
        })
        .catch((e) => {
          console.log(e);
          toast.error("抱歉，该页面暂时不支持访问", { timeout: 2000 });
          router.push({ name: "home" });
        });
    };
    const getColor = (info) => {
      switch (info.type) {
        case "birth":
          return "bg-green-100 border-green-200";
        case "event":
          return "bg-indigo-100 border-indigo-200";
        case "death":
          return "bg-red-100 border-red-200";
        default:
          return "bg-blue-100 border-blue-200";
      }
    };
    onMounted(() => {
      getHistoryToadayInfo();
    });
    return {
      ...toRefs(state),
      getColor,
    };
  },
};
</script>
