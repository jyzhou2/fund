<template>
    <el-row class="tac">
        <el-col :span="4">

            <el-menu
                    default-active="2"
                    class="el-menu-vertical-demo"
                    @open="handleOpen"
                    @close="handleClose">
                <el-menu-item index="2">
                    <i class="el-icon-star-off"></i>

                    <span slot="title" @click="jumpto_data_analysize()">基金筛选</span>
                </el-menu-item>
                <el-menu-item index="3">
                    <i class="el-icon-s-data"></i>
                    <span slot="title" @click="get_article_list_for_data()">数据分析</span>
                </el-menu-item>
                <el-menu-item index="4">
                    <i class="el-icon-s-platform"></i>
                    <span slot="title">服务架构</span>
                </el-menu-item>
                <el-menu-item index="5">
                    <i class="el-icon-setting"></i>
                    <span slot="title" @click="get_article_list_for_laravel()">Laravel</span>
                </el-menu-item>

                <el-menu-item index="6">
                    <i class="el-icon-s-open"></i>
                    <span slot="title" @click="get_article_list_for_python()">Python基础</span>
                </el-menu-item>
                <el-menu-item index="7">
                    <i class="el-icon-info"></i>
                    <span slot="title" @click="get_article_list_for_vue()">VUE</span>
                </el-menu-item>

            </el-menu>
        </el-col>
        <el-col :span="32">
            <div>
                <router-view>
                    <Index/>
                </router-view>
            </div>
        </el-col>
    </el-row>

</template>
<script>
    export default {
        methods: {
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },
            jumpto_data_analysize() {
                location.href = "/JiJinList/JiJinAnalysize"
            },
            get_article_list_for_data() {
                location.href = "/JiJinList/articleList/1"  // 数据分析
            },
            get_article_list_for_python() {
                location.href = "/JiJinList/articleList/3"  // python

            },
            get_article_list_for_laravel() {
                location.href = "/JiJinList/articleList/2"  // laravel

            }, get_article_list_for_vue() {
                location.href = "/JiJinList/articleDetail/1"  // laravel
                //   location.href = "/JiJinList/articleList/4"  // laravel

            }

        }
    }
</script>



