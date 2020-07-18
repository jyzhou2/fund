import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router.js'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import VueAxios from 'vue-axios'


Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(ElementUI)

Vue.config.productionTip = false
new Vue({
    router,
    render: h => h(App),

}).$mount('#app')
