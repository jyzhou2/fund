<template>
    <div>
        <div id="nav">

            <b-tabs  content-class="mt-3">
                <b-tab @click="jumpto_data_JiJinList()" title="基金数据搜索" active>

                </b-tab>
                <b-tab title="数据分析知识" active>
                    <el-row>
                        <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">
                            <el-card :body-style="{ padding: '0px' }">
                                <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                                     class="image">
                                <div style="padding: 14px;">
                                    <span>好吃的汉堡</span>
                                    <div class="bottom clearfix">
                                        <time class="time">{{ currentDate }}</time>
                                        <el-button type="text" class="button">操作按钮</el-button>
                                    </div>
                                </div>
                            </el-card>
                        </el-col>
                    </el-row>
                </b-tab>
                <b-tab title="实时财经消息"><p>I'm a disabled tab!</p></b-tab>
            </b-tabs>

        </div>

    </div>

</template>

<style>
    .time {
        font-size: 13px;
        color: #999;
    }

    .bottom {
        margin-top: 13px;
        line-height: 12px;
    }

    .button {
        padding: 0;
        float: right;
    }

    .image {
        width: 100%;
        display: block;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }
</style>

<script>
    //  var self;
    export default {
        created: function () {
            //  self = this

        },
        data() {
            return {
                currentDate: new Date()
            }
        },
        name: "ArticleList",
        methods: {
            jumpto_data_JiJinList() {
                window.location.href = '/JiJinLIst';
            }
        }
    }
</script>
