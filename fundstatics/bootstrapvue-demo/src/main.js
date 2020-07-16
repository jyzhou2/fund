import Vue from 'vue'
import App from './App.vue'
import  BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import routes from './router'
import VueRouter from 'vue-router'

Vue.use(BootstrapVue)
Vue.use(VueRouter)
const routers= new VueRouter({
  mode:'history',
  routes:routes
})

Vue.config.productionTip = false
new Vue({
  render: h => h(App),
  routers,

}).$mount('#app')
