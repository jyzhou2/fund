import Vue from 'vue'
import Router from 'vue-router'
import JiJinList from './components/JiJinList'
import helloWorld from './components/Index'
import ArticleList from './components/ArticleList'
import ArticleDetail from './components/ArticleDetail'
import vueList from './components/VueList'
import JiJinAnalysize from './components/JiJinAnalysize'
import editor from './components/editormd'

Vue.use(Router)
export default new Router({
        mode: 'history',
        routes: [
            {
                path: '/JiJinList',
                name: 'JiJinList',
                component: JiJinList,
                children: [
                    {
                        path: 'JiJinAnalysize',
                        name: 'JiJinAnalysize',
                        component: JiJinAnalysize,
                    },
                ]
            },
            {
                path: '/',
                name: 'home',
                component: helloWorld
            },
            {
                path: '/ArticleList',
                name: 'articleLIst',
                component: ArticleList
            }
            ,
            {
                path: '/ArticleDetail',
                name: 'ArticleDetail',
                component: ArticleDetail
            }
            ,
            {
                path: '/vue',
                name: 'vue',
                component: vueList
            } ,
            {
                path: '/md',
                name: 'md',
                component: editor
            }
        ]
    }
)

