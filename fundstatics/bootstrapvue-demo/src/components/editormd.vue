<template>
    <div class="markdown-view-box">
        <link rel="stylesheet" href="/static/editor.md/css/editormd.min.css">
        <link rel="stylesheet" href="/static/editor.md/examples/css/style.css"/>
        <link rel="stylesheet" href="/static/editor.md/css/editormd.preview.min.css"/>
        <div id="markdown-view">
            <textarea style="display: none;" id="markdown-view">ebqwkeqwkeqw</textarea>
        </div>
    </div>
</template>
<script>
import scriptjs from 'scriptjs'
let defaultConfig = {
    placeholder: "请输入要发布的内容...",//这里不设置则为默认的
    width: "90%",
    height: 640,
    syncScrolling: "single",
    path: "/static/editor.md/lib/",//lib路径
    imageUpload: true,
    imageFormats: ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
    imageUploadURL: "/fileUpload",//图片上传请求Url
    saveHTMLToTextarea: true,//保存html到textarea
    emoji: true,
    taskList: true,
    tocm: true,         // Using [TOCM]
    tex: true,                   // 开启科学公式TeX语言支持，默认关闭
    flowChart: true,             // 开启流程图支持，默认关闭
    sequenceDiagram: true,// 开启时序/序列图支持，默认关闭
    //下面这一行将使用dark主题
    previewTheme: "dark"
}
export default {
    props: {
        viewId: {
            'type': String,
            'default': 'markdown-view'
        },
        config: { // 编辑器配置
            type: Object
        },
        initData: {
            'type': String
        },
        initDataDelay: {
            'type': Number, // 延迟初始化数据时间，单位毫秒
            'default': 0
        }
    },
    data: function () {
        return {
            doc: {},
            editor: null
        }
    },
    methods: {
        fetchScript: function (url) {
            return new Promise((resolve) => {
                scriptjs(url, () => {
                    resolve()
                })
            })
        },
        getDoc: function () {
            return this.doc
        },
        getConfig: function () {
            return {...defaultConfig, ...this.config}
        },
        forceUpdate: function () {
            this.$forceUpdate()
        },
        initView: function () {
            (async () => {
                await this.fetchScript('/static/editor.md/jquery-2.1.1.min.js')
                await this.fetchScript('/static/editor.md/lib/marked.min.js')
                await this.fetchScript('/static/editor.md/lib/prettify.min.js')
                await this.fetchScript('/static/editor.md/lib/raphael.min.js')
                await this.fetchScript('/static/editor.md/lib/underscore.min.js')
                await this.fetchScript('/static/editor.md/lib/sequence-diagram.min.js')
                await this.fetchScript('/static/editor.md/lib/flowchart.min.js')
                await this.fetchScript('/static/editor.md/lib/jquery.flowchart.min.js')
                await this.fetchScript('/static/editor.md/editormd.min.js')
                this.$nextTick(() => {
                    this.editor = window.editormd.markdownToHTML(this.viewId, this.getConfig())
                })
            })()
        },
        setDoc(doc) {
            if (doc) {
                let vm = this
                vm.doc = doc
                let markdownViewDiv = document.getElementById('markdown-view')
                if (markdownViewDiv) {
                    markdownViewDiv.innerHTML = '<textarea style="display: none;"></textarea>'
                    vm.initView()
                    if (doc.content) {
                        markdownViewDiv.getElementsByTagName('textarea')[0].innerHTML = doc.content
                    }
                }
            }
        },
        showContent(article_content='# 这是测试内容') {
            let vm = this
            let doc = {content:article_content }
            vm.doc = doc
            let markdownViewDiv = document.getElementById('markdown-view')
            if (markdownViewDiv) {
                markdownViewDiv.innerHTML = '<textarea style="display: none;"></textarea>'
                vm.initView()
                if (doc.content) {
                    markdownViewDiv.getElementsByTagName('textarea')[0].innerHTML = doc.content
                }
            }
        }
    },
    mounted: function () {
        let vm = this
        vm.showContent()
    }
}
</script>