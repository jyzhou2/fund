import Vue from 'vue'
import Router from 'vue-router'
import JiJinList from './components/JiJinList'
import helloWorld from './components/Index'
import ArticleList from './components/ArticleList'
import ArticleDetail from './components/ArticleDetail'

Vue.use(Router)
export default new Router({
        mode: 'history',
        routes: [
            {
                path: '/JiJinList',
                name: 'JiJinList',
                component: JiJinList
            },
            {
                path: '/',
                name: 'home',
                component: helloWorld
            },
            {
                path:'/ArticleList',
                name:'articleLIst',
                component:ArticleList
            }
            ,
            {
                path:'/ArticleDetail',
                name:'ArticleDetail',
                component:ArticleDetail
            }
             ,
            {
                path:'/vue',
                name:'vue',
                component:ArticleList
            }
        ]
    }
)

