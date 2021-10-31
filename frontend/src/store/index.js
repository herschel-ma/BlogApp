import { createStore } from 'vuex'
import * as types from "./mutation-types"
import axios from 'axios'
import Cookies from 'js-cookie'
import router from '@/routers'


export default createStore({
  state: {
    pending: false,
    isLoggedIn: localStorage.getItem('token')
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
      state.isLoggedIn = false
    },
    [types.GITHUB_LOGGEDIN](state) {
      state.isLoggedIn = true
    }
  },
  actions: {
    login({ commit }, user) {
      commit(types.LOGIN);
      axios.post('/rest-auth/login/', {
        username: user.username,
        password: user.password
      }, {
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "X-CSRFTOKEN": Cookies.get('csrftoken'),
        }
      }).then(response => {
        localStorage.setItem('token', response.data.key);
        commit(types.LOGIN_SUCCESS);
        console.log('backend auth sussessful. ');
        router.push({ name: 'home' })
      }).catch(response => {
        if (response.status === 400) {
          console.log("No authorized.");
        } else if (response.status === 403) {
          console.log('You are not suposed to see this message. Contact Administrater please');
        }
      })
    },
    logout({ commit }) {
      localStorage.removeItem('token');
      localStorage.clear()
      commit(types.LOGOUT);
    },
    githubLoggedIn(context) {
      if (Cookies.get('token')) {
        localStorage.setItem("token", Cookies.get('token'))
        Cookies.remove('token')
        context.commit(types.GITHUB_LOGGEDIN)
      }
    }
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn
  }
})
