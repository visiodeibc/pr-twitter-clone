import Vue from 'vue';
import VueRouter from 'vue-router';

import Dashboard from '@/views/Dashboard';
import Home from '@/views/Home.vue';
import Login from '@/views/Login';
import Note from '@/views/Note';
import Profile from '@/views/Profile';
import Register from '@/views/Register';

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
    path: '/note/:id',
    name: 'Note',
    component: Note,
    meta: {requiresAuth: true},
    props: true,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;