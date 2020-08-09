<template>
    <div>
        <div id="nav">

            <b-tabs content-class="mt-3">
                <b-tab  title="基金数据搜索" active>

                </b-tab>
                <b-tab title="数据分析知识" active>
                    <div>
                        <Editormd  ref="markdownView"></Editormd>

                    </div>
                </b-tab>
                <b-tab title="实时财经消息"><p>I'm a disabled tab!</p></b-tab>
            </b-tabs>

        </div>

    </div>

</template>

<script>

    import Editormd from "@/components/editormd";


    export default {
        components: {Editormd},
        created: function () {
            //this.mount_select()
        },
        data() {
            return {}
        },
        name: "JiJinList",
        methods: {}
    }
</script>
