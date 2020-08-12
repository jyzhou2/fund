<template>
    <div>
        <BaseInput v-if="!editor.isEditing" ref="markdownView"></BaseInput>
    </div>
</template>

<script>
    import BaseInput from '@/components/editormd.vue'
    var self;
    export default {

        components: {
            BaseInput
        },
        data() {
            return {
                blogEditor: {},
                editor: {'isEditing': false}
            }
        },
        created() {
            self = this
            console.log(1111)
        },

        methods: {
            fillArticleDetail() {
                var type = self.$route.params.article_id
                var theme_url = '/articleDetail?p=w&article_id=' + type;
                self.axios.get(theme_url).then((response) => {
                    self.article_list = response.data.content
                    self.$refs.markdownView.showContent('## 这不是测试内容')

                })
            }
        },
        mounted() {
            self.fillArticleDetail()
        }

    }
</script>

