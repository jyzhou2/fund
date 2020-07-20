<template>
    <div>

        <b-carousel
                id="carousel-1"
                :interval="2000"
                controls
                indicators
                background="#ababab"
                img-width="1024"
                style="text-shadow: 1px 1px 2px #333;"

        >
            <!-- Text slides with image -->
            <b-carousel-slide

                    img-src="http://81.70.21.205:82/img/data_analysize.jpg"
            ></b-carousel-slide>

            <!-- Slides with custom text -->
            <b-carousel-slide

                    img-src="http://81.70.21.205:82/img/python.jpeg">

            </b-carousel-slide>

            <!-- Slides with image only -->
            <b-carousel-slide

                    img-src="http://81.70.21.205:82/img/laravel.png"></b-carousel-slide>

            <!-- Slides with img slot -->

        </b-carousel>


        <br>
        <br>


        <div class="text-center">
            <h2>专栏介绍
                <b-badge>New</b-badge>
            </h2>

            <h6>Column introduction
                <b-badge>New</b-badge>
            </h6>
        </div>
        <b-container>
            <div>
                <b-row>
                    <div v-bind:key="data.index" v-for="data in meals">
                        <b-col l="3">

                            <b-card
                                    v-bind:title="data.strCategory"
                                    v-bind:img-src="data.strCategoryThumb"
                                    img-alt="Image"
                                    img-top
                                    img-height="200"
                                    tag="article"
                                    style="max-width: 20rem;"
                                    class="mb-2">
                                <b-card-text>{{data.desc}}</b-card-text>

                                <b-button v-bind:href="data.href"  variant="primary">查看详情</b-button>


                            </b-card>

                        </b-col>
                    </div>
                </b-row>
            </div>

        </b-container>


    </div>


</template>
<style>
    .w-100 {
        height: 400px !important;;
    }
</style>
<script>

    export default {
        methods: {

        },
        data() {
            return {
                meals: [
                    {
                        'title': '基金数据分析',
                        'strCategoryThumb': 'http://81.70.21.205:82/img/data_analysize.jpg',
                        'desc': '111'
                    }

                ]
            };
        },
        mounted() {
            this.meals = [
                {
                    'title': '基金数据分析',
                    'strCategoryThumb': 'http://81.70.21.205:82/img/data_analysize.jpg',
                    'desc': '数据分析思考和实现过程',
                    'href':'JiJinList'
                },
                {
                    'title': 'Python 记录',
                    'strCategoryThumb': 'http://81.70.21.205:82/img/python.jpeg',
                    'desc': '记录数据分析过程中的技术问题',
                    'href':'python'

                },
                {
                    'title': 'Laravel心得',
                    'strCategoryThumb': 'http://81.70.21.205/img/laravel.png',
                    'desc': '实际工作中遇到的Laravel问题',
                    'href':'laravel'

                },

            ];

        }
    }
</script>