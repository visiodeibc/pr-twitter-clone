import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import notes from './modules/tweets';
import users from './modules/users';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    tweets,
    users,
  },
  plugins: [createPersistedState()]
});