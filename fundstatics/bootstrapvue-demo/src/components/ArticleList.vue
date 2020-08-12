<template>
    <div>
        <el-card class="box-card" :key="item.title" v-for="item in article_list">
            <span class="title">{{item.title}}</span>
            <div class="div_updated_at">
                <span class="update_time">{{item.updated_at}}</span>
            </div>
             <div class="div_content">
                <span class="content">{{item.sub_title}}</span>
            </div>
             <div class="div_view">
                <span class="view_btn" @click="get_article_detail(item.article_id)">查看详情</span>
            </div>
        </el-card>


    </div>

</template>
<style>
    .text {
        font-size: 14px;
    }

    .div_content{

    }
    .content{

    }
    .div_updated_at {
        margin-left: 82%;
    }
    .div_view{
        margin-left: 90%;
        font-size: 10px;
        color: cornflowerblue;
    }
    .update_time{
        font-size: 10px;
    }
    .title {
        font-size: 20px;
        text-align: center;
        margin-left: 40%;
    }

    .item {
        padding: 18px 0;
    }

    .box-card {
        width: 960px;
        margin-top: 2%;
        margin-left: 1%;
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
            get_article_list() {
                var type = self.$route.params.cate
                var theme_url = '/articleList?p=w&cate_id=' + type;
                self.axios.get(theme_url).then((response) => {
                    self.article_list = response.data.data
                })
            },
            get_article_detail(article_id){
                console.log(article_id)
                location.href="/JiJinList/ArticleDetail/"+article_id
            }
        }
    }
</script>
