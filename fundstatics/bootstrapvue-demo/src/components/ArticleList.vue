<template>
    <div>
        <div id="nav">

            <b-tabs content-class="mt-3">
                <b-tab @click="jumpto_data_JiJinList()" title="基金数据搜索" active>

                </b-tab>
                <b-tab title="数据分析知识" active>
                    <el-row>
                        <el-col :span="8" v-for="(o, index) in article_list" :key="o" :offset="index > 0 ? 2 : 0">
                            <el-card :body-style="{ padding: '0px' }">
                                <img :src="o.default_img"
                                     class="image">
                                <div style="padding: 14px;">
                                    <span>{{o.title}}</span>

                                    <div class="right clearfix">
                                        <span style="font-size: 14px">{{o.sub_title}}</span>

                                       <!-- <time class="time" style="margin-left: 0%">{{ o.updated_at }}</time>
                                       -->
                                        <el-button type="text" @click="jumpToArticle(o.article_id)" class="button">查看详情</el-button>
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
    var self;
    export default {
        created: function () {
            self = this
            self.get_article_list()
        },
        data() {
            return {
                currentDate: new Date(),
                article_list: []
            }
        },
        name: "ArticleList",
        methods: {
            jumpto_data_JiJinList() {
                window.location.href = '/JiJinLIst';
            },
            get_article_list() {
                var theme_url = '/articleList?p=w&cate_id=1';
                self.axios.get(theme_url).then((response) => {
                    self.article_list = response.data.data
                })
            },
            jumpToArticle(article_id){
                window.location.href = '/ArticleDetail?article_id='+article_id;

            }
        }
    }
</script>
