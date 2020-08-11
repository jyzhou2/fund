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
        methods: {},
        mounted() {
            vm.$refs.markdownView.showContent('## 这不是测试内容')
        }

    }
    //https://www.jb51.net/article/178777.htm
</script>

