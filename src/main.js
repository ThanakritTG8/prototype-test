// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueApexCharts from 'vue-apexcharts'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { NavbarPlugin } from 'bootstrap-vue'
import { BNavbar } from 'bootstrap-vue'
import axios from 'axios'
import VueDropdown from 'vue-dynamic-dropdown'

import 'animate.css'
import 'fullpage-vue/src/fullpage.css'
import VueFullpage from 'fullpage-vue'

import VueTextTransition from 'vue-text-transition'
Vue.component('vue-text-transition', VueTextTransition)
Vue.use(VueFullpage)
Vue.component('vue-dropdown', VueDropdown);
Vue.component('b-navbar', BNavbar)

Vue.use(NavbarPlugin)

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
// Install ApexChart
Vue.component('apexchart', VueApexCharts)
Vue.prototype.$axios = axios
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
