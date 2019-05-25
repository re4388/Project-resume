import Vue from 'vue';
import axios from 'axios';
import App from './App';

// 把api base 跟axios連在一起
axios.defaults.baseURL = 'http://api.openweathermap.org/data/2.5';

// if the env is not web, use electron, nodejs moduel or vue-electron module
if (!process.env.IS_WEB) Vue.use(require('vue-electron'));

// bind axios to vue.http
Vue.http = Vue.prototype.$http = axios;
// set vue config
Vue.config.productionTip = false;



/* eslint-disable no-new */

// mount app id to main.js
new Vue({
  components: { App },
  template: '<App/>',
}).$mount('#app');