<template>
    <el-row class="tac">
        <el-col :span="4">

            <el-menu
                    default-active="2"
                    class="el-menu-vertical-demo"
                    @open="handleOpen"
                    @close="handleClose">
                <el-menu-item index="2">
                    <i class="el-icon-menu"></i>
                    <span slot="title" @click="jumpto_data_analysize()">基金筛选</span>
                </el-menu-item>
                <el-menu-item index="2">
                    <i class="el-icon-menu"></i>
                    <span slot="title">数据分析</span>
                </el-menu-item>
                <el-menu-item index="2">
                    <i class="el-icon-menu"></i>
                    <span slot="title">服务架构</span>
                </el-menu-item>
                <el-menu-item index="2">
                    <i class="el-icon-menu"></i>
                    <span slot="title">Laravel</span>
                </el-menu-item>

                <el-menu-item index="2">
                    <i class="el-icon-menu"></i>
                    <span slot="title">Python基础</span>
                </el-menu-item>
                <el-menu-item index="2">
                    <i class="el-icon-menu"></i>
                    <span slot="title">VUE</span>
                </el-menu-item>

            </el-menu>
        </el-col>
        <el-col :span="32">
            <router-view>
                <Index/>
            </router-view>
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
            jumpto_data_analysize(){
                location.href="/JiJinList/JiJinAnalysize"
            }
        }
    }
</script>



