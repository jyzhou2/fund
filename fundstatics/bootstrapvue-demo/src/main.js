import Vue from 'vue'
import App from './App.vue'
import  BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueRouter from 'vue-router';
const User = {
  template: '<div>User {{ $route.params.id }}</div>'
}

const router = new VueRouter({
  routes: [
    {
      path: '/user/:userId',
      name: 'user',
      component: User
    }
  ]
})

Vue.use(BootstrapVue)
Vue.use(router)
Vue.config.productionTip = false
new Vue({
  render: h => h(App),

}).$mount('#app')
