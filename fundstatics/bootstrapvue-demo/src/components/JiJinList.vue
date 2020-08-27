<template>
    <el-row class="tac">
        <el-col :span="4">

            <el-menu
                    :default-active="default_active"
                    :active="navselected"
                    class="el-menu-vertical-demo"
                    @open="handleOpen"
                    @select="selectItems"
                    @close="handleClose">
                <el-menu-item index="1" @click="jumpto_data_analysize()">
                    <i class="el-icon-star-off"></i>

                    <span slot="title">基金筛选</span>
                </el-menu-item>
                <el-menu-item index="2" @click="get_article_list_for_data()">
                    <i class="el-icon-s-data"></i>
                    <span slot="title">数据分析</span>
                </el-menu-item>
                <el-menu-item index="3" @click="get_article_list_for_struct()">
                    <i class="el-icon-s-platform"></i>
                    <span slot="title">服务架构</span>
                </el-menu-item>
                <el-menu-item index="4" @click="get_article_list_for_laravel()">
                    <i class="el-icon-setting"></i>
                    <span slot="title">Laravel</span>
                </el-menu-item>

                <el-menu-item index="5" @click="get_article_list_for_python()">
                    <i class="el-icon-s-open"></i>
                    <span slot="title">Python基础</span>
                </el-menu-item>
                <el-menu-item index="6" @click="get_article_list_for_vue()">
                    <i class="el-icon-info"></i>
                    <span slot="title">VUE</span>
                </el-menu-item>

            </el-menu>
        </el-col>
        <el-col :span="32" style="width: 80%">
            <div>
                <router-view>
                    <Index/>
                </router-view>
            </div>
        </el-col>
    </el-row>

</template>
<script>
    let vm;
    export default {
        created() {
            vm = this
            // 设置选中状态
            vm.navselected = vm.index_to_path[this.$route.path]
        },
        data() {
            return {
                navselected: "1",
                default_active: "1",
                index_to_path: {
                    "/JiJinList/JiJinAnalysize": "1",
                    "/JiJinList/articleList/1": "2",
                    "/JiJinList/articleList/2": "4",
                    "/JiJinList/articleList/3": "5",
                    "/JiJinList/articleList/5": "3",

                    "/JiJinList/articleList/4": "6",
                }
            }
        },
        mounted() {
            vm.default_active = vm.index_to_path[this.$route.path]
        },
        methods: {
            selectItems(index) {
                vm.navselected = index
            },
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
                //location.href = "/JiJinList/articleDetail/1"  // laravel
                location.href = "/JiJinList/articleList/4"  // laravel

            }
            , get_article_list_for_struct() {
                location.href = "/JiJinList/articleList/5"  // 服务架构

            }

        }
    }
</script>



