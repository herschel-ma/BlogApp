import { createStore } from "vuex";
import * as types from "./mutation-types";
import axios from "axios";
import Cookies from "js-cookie";
import router from "@/routers";

const store = createStore({
  state() {
    return {
      pending: false,
      isLoggedIn: localStorage.getItem("token"),
      token: "",
      user_name: "",
      categorys: [],
      tags: [],
      delTag: 0,
    };
  },
  mutations: {
    [types.LOGIN](state) {
      state.pending = true;
    },
    [types.LOGIN_SUCCESS](state) {
      state.isLoggedIn = true;
      state.pending = false;
    },
    [types.LOGOUT](state) {
      state.isLoggedIn = false;
    },
    [types.GITHUB_LOGGEDIN](state) {
      state.isLoggedIn = true;
    },
    [types.S_USERNAME](state, user_name) {
      state.user_name = user_name;
    },
    [types.S_CATEGORIES](state, categorys) {
      state.categorys = categorys;
    },
    [types.S_TAGS](state, tags) {
      state.tags = tags;
    },
    [types.S_DEL_TAG](state, tag) {
      state.delTag = tag;
    },
    [types.D_DEL_TAG](state) {
      state.delTag = 0;
    },
  },
  actions: {
    login({ commit }, user) {
      commit(types.LOGIN);
      axios
        .post(
          "/rest-auth/login/",
          {
            username: user.username,
            password: user.password,
          },
          {
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
              "X-CSRFTOKEN": Cookies.get("csrftoken"),
            },
          }
        )
        .then((response) => {
          localStorage.setItem("token", response.data.key);
          commit(types.LOGIN_SUCCESS);
          console.log("backend auth sussessful. ");
          router.push({ name: "home" });
        })
        .catch((response) => {
          if (response.status === 400) {
            console.log("No authorized.");
          } else if (response.status === 403) {
            console.log(
              "You are not suposed to see this message. Contact Administrater please"
            );
          }
        });
    },
    logout({ commit }) {
      localStorage.removeItem("token");
      localStorage.removeItem("user_name");
      localStorage.clear();
      commit(types.LOGOUT);
    },
    githubLoggedIn(context) {
      if (Cookies.get("token")) {
        localStorage.setItem("token", Cookies.get("token"));
        Cookies.remove("token");
        context.commit(types.GITHUB_LOGGEDIN);
      }
    },
    storeUserName({ commit }, user_name) {
      localStorage.setItem("user_name", user_name);
      commit(types.S_USERNAME, user_name);
    },
    storeCategories({ commit }, categories) {
      commit(types.S_CATEGORIES, categories);
    },
    storeTags({ commit }, tags) {
      commit(types.S_TAGS, tags);
    },
    storeDelTag({ commit }, tag) {
      commit(types.S_DEL_TAG, tag);
    },
    deleteDeleteTag({ commit }) {
      commit(types.S_DEL_TAG);
    },
  },
  getters: {
    isLoggedIn: (state) => state.isLoggedIn,
    categorys: (state) => state.categorys,
    tags: (state) => state.tags,
    delTag: (state) => state.delTag,
  },
});

export default store;
