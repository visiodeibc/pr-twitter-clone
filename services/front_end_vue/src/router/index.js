import Vue from 'vue';
import VueRouter from 'vue-router';

import Dashboard from '@/views/Dashboard';
import Home from '@/views/Home.vue';
import Login from '@/views/Login';
import Tweet from '@/views/Tweet';
import Profile from '@/views/Profile';
import Register from '@/views/Register';
import EditTweet from '@/views/EditTweet';

import store from '@/store';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: "Home",
    component: Home,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {requiresAuth: true},
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {requiresAuth: true},
  },
  {
    path: '/tweet/:id',
    name: 'Tweet',
    component: Tweet,
    meta: {requiresAuth: true},
    props: true,
  },
  {
    path: '/tweet/:id',
    name: 'EditTweet',
    component: EditTweet,
    meta: {requiresAuth: true},
    props: true,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;