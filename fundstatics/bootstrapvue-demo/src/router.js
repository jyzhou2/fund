import Vue from 'vue'
import Router from 'vue-router'
import JiJinList from './components/JiJinList'
import helloWorld from './components/Index'
import ArticleList from './components/ArticleList'
import ArticleDetail from './components/ArticleDetail'
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
                    {
                        path: 'articleList/:cate/',
                        name: 'articleList',
                        component: ArticleList,
                    },

                    {
                        path: '/ArticleDetail/:article_id',
                        name: 'ArticleDetail',
                        component: ArticleDetail
                    }

                ]
            },
            {
                path: '/',
                name: 'home',
                component: helloWorld
            },
            {
                path: '/testmd',
                name: 'md',
                component: editor
            }
            ,
            {
                path: '/testDetail',
                name: 'testDetail',
                component: ArticleDetail
            }
        ]
    }
)

