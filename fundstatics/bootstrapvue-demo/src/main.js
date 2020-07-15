import Vue from 'vue'
import App from './App.vue'
import  BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import JiJinList from './components/JiJinList'
import VueRouter from 'vue-router';
const router = new VueRouter({
  routes:  [
    {
      path:'/jijininfo_list',
      name:'jijin',
      component:JiJinList
    }
  ]
})
Vue.use(BootstrapVue)
Vue.use(router)
Vue.config.productionTip = false
new Vue({
  render: h => h(App),

}).$mount('#app')
