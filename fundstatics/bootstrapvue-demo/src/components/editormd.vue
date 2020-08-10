<template>
    <div class="markdown-editor-box">
        <link rel="stylesheet" href="/static/editor.md/css/editormd.min.css">
        <div :id="editorId"></div>
    </div>
</template>
<script>
    import scriptjs from 'scriptjs'

    const defaultConfig = {
        width: "100%",
        height: 600,
        path: '/static/editor.md/lib/',
        // theme: 'dark',
        // previewTheme: 'dark',
        // editorTheme: 'pastel-on-dark',
        markdown: '',      // 預設填充內容
        lineWrapping: true, // 編輯框不換行
        codeFold: true,                 // 程式碼摺疊
        placeholder: '請輸入...',
        syncScrolling: true,
        saveHTMLToTextarea: true,       // 儲存 HTML 到 Textarea
        searchReplace: true,
        watch: true,                                // 實時預覽
        htmlDecode: "style,script,iframe|on*",      // 開啟 HTML 標籤解析，為了安全性，預設不開啟
        toolbar: true,                  //工具欄
        previewCodeHighlight: true,     // 預覽 HTML 的程式碼塊高亮，預設開啟
        emoji: true,
        taskList: true,
        tocm: true,                     // Using [TOCM]
        tex: true,                      // 開啟科學公式TeX語言支援，預設關閉
        flowChart: true,                // 開啟流程圖支援，預設關閉
        sequenceDiagram: true,          // 開啟時序/序列圖支援，預設關閉,
        // dialogLockScreen: false,      // 設定彈出層對話方塊不鎖屏，全域性通用，預設為true
        // dialogShowMask: false,        // 設定彈出層對話方塊顯示透明遮罩層，全域性通用，預設為true
        // dialogDraggable: false,       // 設定彈出層對話方塊不可拖動，全域性通用，預設為true
        // dialogMaskOpacity: 0.4,       // 設定透明遮罩層的透明度，全域性通用，預設值為0.1
        // dialogMaskBgColor: "#000",    // 設定透明遮罩層的背景顏色，全域性通用，預設為#fff
        // imageUpload: false,
        // imageFormats: ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        // imageUploadURL: "./php/upload.php",
        // onload: function() {
        //    // this.fullscreen();
        //    // this.unwatch();
        //    // this.watch().fullscreen();
        //    // this.setMarkdown("#PHP");
        //    // this.width("100%");
        //    // this.height(480);
        //    // this.resize("100%", 640);
        // },
    };
    let vm;
    export default {
        name: 'BaseInput',
        props: {
            editorId: {
                'type': String,
                'default': 'markdown-editor'
            },
            onchange: { // 內容改變時回撥，返回（html, markdown, text）
                type: Function
            },
            config: { // 編輯器配置
                type: Object
            },
            initData: {
                'type': String
            },
            initDataDelay: {
                'type': Number, // 延遲初始化資料時間，單位毫秒
                'default': 0
            }
        },
        data: function () {
            return {
                editor: null,
                timer: null,
                doc: {},
                jsLoadOver: false
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
            getConfig: function () {
                return {...defaultConfig, ...this.config}
            },
            getEditor: function () {
                return this.editor
            },
            getDoc: function () {
                return this.doc
            },
            watch: function () {
                return this.editor.watch()
            },
            unwatch: function () {
                return this.editor.unwatch()
            },
            previewing: function () {
                return this.editor.previewing()
            },
            getHTML: function () {
                return this.editor.getHTML()
            },
            getMarkdown: function () {
                return this.editor.getMarkdown()
            },
            setMarkdown: function (markdown) {
                return this.editor.setMarkdown(markdown)
            },
            init() {

                let doc = {'content': '312313123'}
                vm.doc = doc
                let md = doc.content
                vm.initEditor(md)

            },
            initEditor: function (markdown) {
                let vm = this
                let config = vm.getConfig()
                if (markdown) {
                    config.markdown = markdown
                }
                (async () => {
                    await vm.fetchScript('/static/editor.md/jquery.min.js')
                    await vm.fetchScript('/static/editor.md/editormd.min.js')
                    vm.jsLoadOver = true
                    vm.$nextTick(() => {
                        vm.editor = window.editormd(vm.editorId, config)
                        vm.editor.on('load', () => {
                            setTimeout(() => { // hack bug: 一個頁面多個編輯器只能初始化其中一個數據問題
                                vm.initData && vm.editor.setMarkdown(vm.initData)
                            }, vm.initDataDelay)
                        })
                        vm.onchange && vm.editor.on('change', () => {
                            let html = vm.editor.getPreviewedHTML()
                            vm.onchange({
                                markdown: vm.editor.getMarkdown(),
                                html: html,
                                text: window.$(html).text()
                            })
                        })
                    })
                })()
            }
        },
        mounted: function () {
            vm = this

            vm.init()
            vm.timer = setInterval(function () {

            }, 80)
        },
        destroyed: function () {
            let vm = this
            if (vm.timer != null) {
                window.clearInterval(vm.timer)
                vm.timer = null
            }
        }
    }
</script>