import { createStore } from "vuex";
import * as types from "./mutation-types";
import axios from "axios";
import { useToast } from "vue-toastification";
import Cookies from "js-cookie";
// import router from "@/routers";

const toast = useToast();
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
      delCata: 0,
      usersInfo: [],
      searchWord: "",
      userId: 0,
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
    [types.S_DEL_CATA](state, delCata) {
      state.delCata = delCata;
    },
    [types.D_DEL_CATA](state) {
      state.delCata = 0;
    },
    [types.S_USERS](state, usersInfo) {
      state.usersInfo = usersInfo;
    },
    [types.S_SEARCH_WORD](state, word) {
      state.searchWord = word;
    },
    [types.D_SEARCH_WORD](state) {
      state.searchWord = "";
    },
    [types.S_USERID](state, id) {
      state.userId = id;
    },
  },
  actions: {
    login({ commit }, user) {
      commit(types.LOGIN);
      if (user.username === undefined || user.username === "") {
        toast.error("用户名不能为空", { timeout: 2000 });
        return;
      }
      if (user.password === undefined || user.password === "") {
        toast.error("密码不能为空", { timeout: 2000 });
        return;
      }
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
          toast.success("登录成功", { timeout: 2000 });
          window.location.href = "/";
        })
        .catch((response) => {
          if (response.response.data.non_field_errors) {
            toast.error(response.response.data.non_field_errors[0], {
              timeout: 2000,
            });
          } else if (response.response.data.username) {
            toast.error("昵称有误，请重试", { timeout: 2000 });
          } else if (response.response.data.password) {
            toast.error("密码有误，请重试", { timeout: 2000 });
          }
          if (response.status === 400) {
            console.log("Authentication failed");
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
    storeDelCata({ commit }, cata) {
      commit(types.S_DEL_CATA, cata);
    },
    deleteDeleteCata({ commit }) {
      commit(types.S_DEL_CATA);
    },
    storeUsers({ commit }, usersInfo) {
      commit(types.S_USERS, usersInfo);
    },
    storeSearchWord({ commit }, word) {
      commit(types.S_SEARCH_WORD, word);
    },
    deleteSearchWord({ commit }) {
      commit(types.D_SEARCH_WORD);
    },
    storeUserId({ commit }, id) {
      commit(types.S_USERID, id);
    },
  },
  getters: {
    isLoggedIn: (state) => state.isLoggedIn,
    categorys: (state) => state.categorys,
    tags: (state) => state.tags,
    delTag: (state) => state.delTag,
    delCate: (state) => state.delCata,
    usersInfo: (state) => state.usersInfo,
    searchWord: (state) => state.searchWord,
    userId: (state) => state.userId,
    username: (state) => state.user_name,
  },
});

export default store;
