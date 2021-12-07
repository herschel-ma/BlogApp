<template>
  <svg :width="width" :height="height" @mousemove="listener($event)">
    <a :href="tag.href" v-for="tag in tags" :key="tag">
      <text
        :x="tag.x"
        :y="tag.y"
        :font-size="20 * (600 / (600 - tag.z))"
        :fill-opacity="(400 + tag.z) / 600"
        :stroke="tag.color"
      >
        {{ tag.text }}
      </text>
    </a>
  </svg>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";
export default {
  props: {
    width: {
      type: Number,
      required: true,
    },
    height: {
      type: Number,
      required: true,
    },
    RADIUS: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      tagsNum: 20,
      speedX: Math.PI / 360,
      speedY: Math.PI / 360,
      tags: [],
    };
  },
  computed: {
    CX() {
      return this.width / 2;
    },
    CY() {
      return this.height / 2;
    },
  },
  created() {
    //初始化标签位置
    let tags = [];
    const colors = [
      "red",
      "blue",
      "gray",
      "orange",
      "yellow",
      "purple",
      "blank",
      "pink",
      "peach",
      "cherry",
      "plum",
      "maize",
      "bluish",
      "ultramarine",
      "raisin",
      "lividity",
    ];
    axios
      .get("api/tag", {
        headers: {
          "Content-Type": "Application/json",
          "X-CSRFTOKEN": Cookies.get("csrftoken"),
          Authorization: "Token " + this.$store.state.isLoggedIn,
        },
      })
      .then((res) => {
        this.$store.dispatch("storeTags", res.data);
        this.tagsNum = res.data.length;
        for (let i = 0; i < this.tagsNum; i++) {
          let tag = {};
          let k = -1 + (2 * (i + 1) - 1) / this.tagsNum;
          let a = Math.acos(k);
          let b = a * Math.sqrt(this.tagsNum * Math.PI);
          tag.text = res.data[i].name;
          tag.x = this.CX + this.RADIUS * Math.sin(a) * Math.cos(b);
          tag.y = this.CY + this.RADIUS * Math.sin(a) * Math.sin(b);
          tag.z = this.RADIUS * Math.cos(a);
          const index = Math.floor(Math.random() * colors.length);
          tag.color = `${colors[index]}`;
          tag.href = "api/tag/" + res.data[i].id;
          tags.push(tag);
        }
        this.tags = tags;
      })
      .catch((e) => console.log(e));
  },
  mounted() {
    //使球开始旋转
    setInterval(() => {
      this.rotateX(this.speedX);
      this.rotateY(this.speedY);
    }, 17);
  },
  methods: {
    rotateX(speedX) {
      var cos = Math.cos(speedX);
      var sin = Math.sin(speedX);
      for (let tag of this.tags) {
        var y1 = (tag.y - this.CY) * cos - tag.z * sin + this.CY;
        var z1 = tag.z * cos + (tag.y - this.CY) * sin;
        tag.y = y1;
        tag.z = z1;
      }
    },
    rotateY(speedY) {
      var cos = Math.cos(speedY);
      var sin = Math.sin(speedY);
      for (let tag of this.tags) {
        var x1 = (tag.x - this.CX) * cos - tag.z * sin + this.CX;
        var z1 = tag.z * cos + (tag.x - this.CX) * sin;
        tag.x = x1;
        tag.z = z1;
      }
    },
    listener(event) {
      //响应鼠标移动
      var x = event.clientX - this.CX;
      var y = event.clientY - this.CY;
      this.speedX =
        x * 0.0001 > 0
          ? Math.min(this.RADIUS * 0.00002, x * 0.0001)
          : Math.max(-this.RADIUS * 0.00002, x * 0.0001);
      this.speedY =
        y * 0.0001 > 0
          ? Math.min(this.RADIUS * 0.00002, y * 0.0001)
          : Math.max(-this.RADIUS * 0.00002, y * 0.0001);
    },
  },
};
</script>

<style></style>
