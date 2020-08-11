<template>
    <div>
        <el-card class="box-card" :key="item.title" v-for="item in article_list">
            <div>{{item.title}}</div>
        </el-card>


    </div>

</template>
<style>
    .text {
        font-size: 14px;
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
            }
        }
    }
</script>
