<template>
    <div>
        <div id="nav">

            <b-tabs content-class="mt-3">
                <b-tab @click="jumpto_data_JiJinList()" title="基金数据搜索" active>

                </b-tab>
                <b-tab title="数据分析知识" active>

                    <div id="main">
                        <mavon-editor
                                :subfield="false"
                                :boxShadow="false"
                                defaultOpen="preview"
                                :toolbarsFlag="false"
                                :ishljs="true" v-model="value">eqweqweqweq</mavon-editor>

                    </div>

                </b-tab>
                <b-tab title="实时财经消息"><p>I'm a disabled tab!</p></b-tab>
            </b-tabs>

        </div>

    </div>

</template>

<script>

    var self;
    export default {
        created: function () {
            self = this
            self.getArticleDeatil()
        },
        data() {
            return {
                value:'ddadjasdlal',
            }
        },
        name: "ArticleList",
        methods: {
            getArticleDeatil() {

                var theme_url = '/articleDetail?p=w&article_id=1';
                self.axios.get(theme_url).then((response) => {
                    self.value = response.data.data.content
                })
            }
        }
    }
</script>
