<template>
    <div>
        <BaseInput v-if="!editor.isEditing" ref="markdownView"></BaseInput>
    </div>
</template>
<style>
    body{
        text-align: left !important;
    }
</style>

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
                    self.$refs.markdownView.showContent(response.data.data.content)

                })
            }
        },
        mounted() {
            self.fillArticleDetail()
        }

    }
</script>

