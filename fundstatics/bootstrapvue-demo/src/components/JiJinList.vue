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
                                    <b-button @click="search">Search
                                    </b-button>
                                </b-col>
                            </b-row>
                        </b-container>

                        <!--  这里是搜索数结果数据 -->
                        <br>
                        <br>


                            <el-table
                                    v-loading="loading"
                                    :data="items"
                                    style="width: 100%">
                                <el-table-column
                                        prop="name"
                                        label="名称"
                                        width="180">
                                </el-table-column>
                                <el-table-column
                                        prop="guimo"
                                        label="规模"
                                        width="180">
                                </el-table-column>
                                <el-table-column
                                        prop="level"
                                        label="水平(周-月-三月-半年)">
                                </el-table-column>
                                <el-table-column
                                        prop="update_time"
                                        label="更新时间">
                                </el-table-column>
                                <el-table-column
                                        prop="recommand"
                                        label="推荐">
                                </el-table-column>
                            </el-table>


                    </div>

                </b-tab>
                <b-tab title="数据分析知识"><p>I'm the second tab</p></b-tab>
                <b-tab title="实时财经消息"><p>I'm a disabled tab!</p></b-tab>
            </b-tabs>

        </div>

    </div>

</template>
<style>
    .table {
        width: 88%;
    }

    td {
        height: 45px !important;
    }

    tr {
        height: 45px !important;
    }

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
                loading:true,
                theme: [],
                week_selected: null,
                guimo: 5,

                perPage: 3,
                currentPage: 1,
                items: []
            }
        },
        name: "JiJinList",
        methods: {
            //  搜索
            search() {
                var url = "";
                url = 'http://81.70.21.205:82/api/fund_list?p=w&';
                url += 'guimo=' + self.guimo + "&"
                url += 'theme=' + self.theme + "&"
                self.loading = true
                this.axios.get(url).then((response) => {
                    self.loading = false
                    var datas = response.data;
                    datas = datas.data
                    var i = null;
                    self.items = []
                    for (i in datas) {
                        var cur_item = datas[i]
                        self.items.push({
                            'name': cur_item.name,
                            'guimo': cur_item.guimo_number,
                            'level': cur_item.one_week_level + "-" + cur_item.one_month_level + "-" + cur_item.three_months_level + "-" + cur_item.six_months_level,
                            'update_time': cur_item.gsl_update_time,
                            'recommand': '暂无'
                        })
                    }
                })

            },

        }
    }
</script>

