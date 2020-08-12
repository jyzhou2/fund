<template>
    <div>
        <BaseInput v-if="!editor.isEditing" ref="markdownView"></BaseInput>
    </div>
</template>

<script>
    import BaseInput from '@/components/editormd.vue'

    let vm;
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
            vm = this
        },

        methods: {
            fillArticleDetail() {
                var type = vm.$route.params.article_id
                var theme_url = '/articleDetail?p=w&article_id=' + type;
                vm.axios.get(theme_url).then((response) => {
                    vm.article_list = response.data.data
                    vm.$refs.markdownView.showContent('## 这不是测试内容')

                })
            }
        },
        mounted() {
            vm.fillArticleDetail()
        }

    }
    //https://www.jb51.net/article/178777.htm
</script>

