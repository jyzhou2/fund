import Vue from 'vue'
import Router from 'vue-router'
import JiJinList from './components/JiJinList'
import helloWorld from './components/HelloWorld'
Vue.use(Router)
export default new Router({
    mode:'history',
    routes:[
    {
        path:'/JiJinList',
        name:'JiJinList',
        component:JiJinList
    },
        {
        path:'/',
        name:'home',
        component:helloWorld
    }
    ]
    }
)

