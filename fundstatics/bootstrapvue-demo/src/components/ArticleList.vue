<template>
    <div>
        <el-card class="box-card">
            <div v-for="o in 4" :key="o" class="text item">
                {{'列表内容 ' + o }}
            </div>
        </el-card>

        <el-card class="box-card">
            <div v-for="o in 4" :key="o" class="text item">
                {{'列表内容 ' + o }}
            </div>
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
           get_article_list(){
               var type = self.$route.params.cate
               console.log(type)
           }
        }
    }
</script>
