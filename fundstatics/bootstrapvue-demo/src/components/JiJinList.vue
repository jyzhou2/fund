<template>
    <div>
        <div id="nav">

            <b-tabs content-class="mt-3">
                <b-tab title="基金数据搜索" active>

                    <div id="data">
                        <br>

                        <b-container class="bv-example-row">
                            <b-row>
                                <b-col>
                                    <b-form-tags input-id="tags-basic" class="mb-1" no-add-on-enter separator=" "
                                                 placeholder="选择基金主题"
                                                 v-model="theme"></b-form-tags>
                                </b-col>
                                <b-col>
                                    <b-form-input type="number" v-model="guimo"
                                                  placeholder="输入基金规模"></b-form-input>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="week_selected" :options="week_options">


                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="month_selected" :options="month_options">

                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="three_months_selected" :options="three_months_options">

                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="half_year_selected" :options="half_year_options">
                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="year_selected" :options="year_options">
                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-button @click="search">Search
                                    </b-button>
                                </b-col>
                            </b-row>
                        </b-container>


                        <!--  这里是搜索数结果数据 -->

                        <div class="overflow-auto">




                            <b-table
                                    id="my-table"
                                    :items="items"

                                    small
                            ></b-table>

                        </div>
                    </div>

                </b-tab>
                <b-tab title="数据分析知识"><p>I'm the second tab</p></b-tab>
                <b-tab title="实时财经消息"><p>I'm a disabled tab!</p></b-tab>
            </b-tabs>

        </div>

    </div>

</template>
<style>
    #tags-basic {
        height: 25px !important;
    }

    #jijinGuiMo {
        width: 150px;
    }

    #tags-basic {
        width: 150px !important;;
    }

    .bv-example-row {
        margin-left: 0%;
    }

    .overflow-auto {
        margin-left: 1%;

    }

    #nav {
        margin-left: 10%;
    }
</style>
<script>

    var self;
    export default {
        created: function () {
            self = this
        },
        data() {

            return {
                value: [],
                theme:'',
                week_selected: null,
                guimo: 0,
                month_selected: null,
                three_months_selected: null,
                half_year_selected: null,
                year_selected: null,
                week_options: ['正序'],
                month_options: ['正序'],
                three_months_options: ['正序'],
                half_year_options: ['正序'],
                year_options: ['正序'],
                perPage: 3,
                currentPage: 1,
                items: [


                ]
            }
        },
        name: "JiJinList",
        methods: {
            //  搜索
            search() {
                var url="";
                url = 'http://81.70.21.205/api/fund_list?p=w&';
                url +='guimo='+ self.guimo+"&"
                url += 'theme='+self.theme+"&"
                url += 'week_selected='+self.week_selected+"&"

                url+= 'month_selected='+ self.month_selected+"&"
                url+= 'three_months_selected='+ self.three_months_selected+"&"
                url+= 'half_year_selected='+ self.half_year_selected+"&"
                url+= 'year_selected='+ self.year_selected+"&"

                this.axios.get(url).then((response) => {
                    var datas = response.data;
                    datas= datas.data
                    var i=null;
                    self.items = []
                    for(i in datas){
                        var cur_item = datas[i]
                        self.items.push({
                            '名称': cur_item.name,
                            '规模': cur_item.guimo_number,
                            '周水平': cur_item.one_week_level,
                            '月水平': cur_item.one_month_level,
                            '三月水平': cur_item.three_months_level,
                            '半年水平': cur_item.six_months_level,
                            '年水平': cur_item.six_months_level,

                        })
                        console.log(i)
                    }
                })
                /*
                var guimo = self.guimo
                guimo += ''
                var theme = self.theme
                theme += ''
                var week_selected = self.week_selected
                week_selected += ''
                var month_selected = self.month_selected
                month_selected += ''
                var three_months_selected = self.three_months_selected
                three_months_selected += ''
                var half_year_selected = self.half_year_selected
                half_year_selected += ''
                var year_selected = self.year_selected
                year_selected += ''*/
            },

        }
    }
</script>

