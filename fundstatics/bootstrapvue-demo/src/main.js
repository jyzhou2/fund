import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router.js'
import axios from 'axios'
import {Loading} from 'element-ui'
import VueAxios from 'vue-axios'


Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)

let requestCount = 0;
var loading = null;
let timer = null;

function showLoading() {
    if (requestCount === 0) {
        loading = Loading.service({
            spinner: 'mobile-loading',
            background: "rgba(0,0,0,0.8)"
        })
    }
    requestCount++

}

function tryHideLoading() {
    requestCount--
    timer = setTimeout(() => {
        if (requestCount === 0) {
            loading.close()
            clearTimeout(timer)
        }

    })
}

axios.interceptors.request.use(function (config) {
        showLoading()
        return config;
    },
    function (error) {
        return Promise.reject(error)
    })
axios.interceptors.response.use(function (response) {
    tryHideLoading()
    return response

}, function (error) {
    return Promise.reject(error)

})
Vue.config.productionTip = false
new Vue({
    router,
    render: h => h(App),

}).$mount('#app')
