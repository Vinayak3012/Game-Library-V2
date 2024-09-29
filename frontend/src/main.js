import { createApp } from 'vue'
import './style.css'
import './assets/index.css'
import App from './App.vue'
import router from './router'
import { createStore } from 'vuex/dist/vuex.cjs.js'

const store = createStore({
  state() {
    return {
      user: {
        userid: '',
        username: '',
        email: '',
        type: '',
      },
      auth_token: '',
      login_status: false,
    }
  },
  getters: {
    get_user: function (state) {
      return state.user
    },
    get_userid: function (state) {
      return state.user.userid
    },
    get_username: function (state) {
      return state.user.username
    },
    get_email: function (state) {
      return state.user.email
    },
    get_type: function (state) {
      return state.user.type
    },
    // this.$store.getters.get_auth_token ->
    get_auth_token: function (state) {
      return state.auth_token
    },
    get_login_status: function (state) {
      return state.login_status
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('store')) {
        this.replaceState(
          Object.assign(state, JSON.parse(localStorage.getItem('store')))
        )
      } else {
        console.log('store not found !')
      }
    },

    setStateAfterLogin(state, payload) {
      state.user.userid = payload.userid
      state.user.username = payload.username
      state.user.email = payload.email
      state.user.type = payload.type
      state.auth_token = payload.auth_token
      login_status = true
    },
    setStateAfterLogout(state) {
      state.user.userid = ''
      state.user.username = ''
      state.user.email = ''
      state.user.type = ''
      state.auth_token = ''
      login_status = false
    },
  },
  actions: {
    initialize({ commit }) {
      commit('initializeStore')
    },
    set_state_after_login(context, payload) {
      context.commit('setStateAfterLogin', payload)
    },
    set_state_after_logout(context) {
      context.commit('setStateAfterLogout')
    },
  },
})
store.subscribe((mutation, state) => {
  localStorage.setItem('store', JSON.stringify(state))
})

store.dispatch('initialize')

createApp(App).use(router).use(store).mount('#app')

/*
manager.gamevault@gmail.com
user.gamevault@gmail.com


Qa*********

*/
