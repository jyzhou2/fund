<template>
    <div>
        <div id="nav" style="width: 1200px;margin-top: 2%">
            <b-container class="bv-example-row">
                <b-row>
                    <b-col>
                        <el-select v-model="SelectJiJinThemes" filterable allow-create default-first-option
                                   clearable
                                   placeholder="请选择基金主题" style="width:280px">
                            <el-option v-for="item in JiJinThemes" :key="item.title" :label="item.title"
                                       v-bind:value="item.title">
                                <span style="float: left">{{ item.title }}</span>
                                <span style="margin-left:15px;color: #8492a6; font-size: 13px">({{ item.label }})</span>
                            </el-option>
                        </el-select>
                    </b-col>

                      <b-col>
                        <b-form-input type="number" v-model="type" filterable allow-create default-first-option
                                   clearable
                                   placeholder="请选择基金类型" style="width:200px"></b-form-input>
                    </b-col>
                     <b-col>
                        <b-form-input type="number" v-model="guimo"
                                      placeholder="输入基金规模" ></b-form-input>
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
                :data="items"

                v-loading = "loading"

                element-loading-text = "数据正在加载中"
                element-loading-spinner = "el-icon-loading"
                style="width: 100%">
                <el-table-column
                        width="100"
                        label="推荐">

                    <template slot-scope="scope">
                        <el-popover width="100" :ref="`popover-${scope.$index}`" trigger="hover">

                            <template>
                                <img :src="scope.row.jijin_pic"
                                     style="margin-left: 30%;width: 300px;height: 200px"/>
                            </template>

                            <el-button type="text" slot="reference">{{ scope.row.recommand }}</el-button>
                        </el-popover>
                    </template>

                </el-table-column>
                <el-table-column label="名称" width="180">
                    <template slot-scope="scope">
                        <el-button type="text" @click="jumpToJJDM(scope.row.jjdm)"> {{scope.row.name}}
                        </el-button>
                    </template>
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
                        prop="risk_level"
                        label="风险等级">
                </el-table-column>
                <el-table-column
                        prop="update_time"
                        label="更新时间">
                </el-table-column>

            </el-table>
        </div>

    </div>


</template>
<style>
    .table {
        width: 90%;
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
        margin-left: 1%;
        width: 100%;
    }
</style>
<script>
    var self;
    export default {
        created: function () {
            self = this
            this.mount_select()
        },
        data() {
            return {
                value: [],
                loading: false,
                theme: [],
                week_selected: null,
                guimo: 5,
                perPage: 3,
                currentPage: 1,
                items: [
                    ],
                popovershow: true,
                visible: false,
                JiJinThemes: [],
                SelectJiJinThemes: "",
                type:''
            }
        },
        name: "JiJinList",
        methods: {

            //  搜索
            mount_select() {
                var theme_url = "";
                theme_url = 'http://81.70.21.205:82/api/getThemeList?p=w&';
                this.axios.get(theme_url).then((response) => {
                    self.JiJinThemes = response.data.data
                })
            },

            jumpToJJDM(jjdm) {
                window.open("http://fund.eastmoney.com/" + jjdm + ".html")
            },
            search() {
                var url = "";
                url = '/fund_list?p=w&';
                url += 'guimo=' + self.guimo + "&"
                url += 'theme=' + self.SelectJiJinThemes + "&"
                self.loading = true
                self.axios.get(url, {timeout: 300000}).then((response) => {
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
                            'recommand': cur_item.recommand,
                            'jjdm': cur_item.jjdm,
                            'jijin_pic': cur_item.jijin_pic,
                            'risk_level': cur_item.jijin_type
                        })
                    }
                })
            }
        }
    }
</script>