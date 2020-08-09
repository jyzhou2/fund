<template>
    <div>
        <div id="nav">

            <b-tabs content-class="mt-3">
                <b-tab @click="jumpto_data_JiJinList()" title="基金数据搜索" active>

                </b-tab>
                <b-tab title="数据分析知识" active>
                    <Editor :content="content" @change="autoSave" type="editor"></Editor>
                </b-tab>
                <b-tab title="实时财经消息"><p>I'm a disabled tab!</p></b-tab>
            </b-tabs>

        </div>

    </div>

</template>

<script>
    import Editor from '@/components/Editormd'
let self;
    export default {
        components: {Editor},
        created: function () {
            self = this
        },
        data() {
            return {
                content: 'dsdlsdjowdjoediowende',//这里是初始化是编辑器回显内容
            }
        },
        props: {},
        mounted() {
            self.getArticleDeatil()
        },
        methods:
            {
                autoSave(html, text) {
                    console.log(html)
                    console.log(text)
                },
                getArticleDeatil() {
                    var theme_url = '/articleDetail?p=w&article_id=1';
                    self.axios.get(theme_url).then((response) => {
                        self.content = response.data.data.content
                    })
                },

            }
    }
</script>
