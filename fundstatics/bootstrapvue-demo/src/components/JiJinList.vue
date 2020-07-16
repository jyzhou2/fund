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
                                                 v-model="value"></b-form-tags>
                                </b-col>
                                <b-col>
                                    <b-form-input type="number" id="jijinGuiMo" placeholder="输入基金规模"></b-form-input>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="selected" :options="week_options">
                                        <b-form-select-option :value="null">周分析</b-form-select-option>

                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="selected" :options="week_options">
                                        <b-form-select-option :value="null">月分析</b-form-select-option>

                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="selected" :options="week_options">
                                        <b-form-select-option :value="null">三月分析</b-form-select-option>
                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="selected" :options="week_options">
                                        <b-form-select-option :value="null">半年分析</b-form-select-option>
                                    </b-form-select>
                                </b-col>
                                <b-col>
                                    <b-form-select v-model="selected" :options="week_options">
                                        <b-form-select-option :value="null">年分析</b-form-select-option>
                                    </b-form-select>
                                </b-col>
                            </b-row>
                        </b-container>


                        <!--  这里是搜索数结果数据 -->

                        <div class="overflow-auto">


                            <p class="mt-3">Current Page: {{ currentPage }}</p>

                            <b-table
                                    id="my-table"
                                    :items="items"
                                    :per-page="perPage"
                                    :current-page="currentPage"
                                    small
                            ></b-table>
                            <b-pagination
                                    v-model="currentPage"
                                    :total-rows="rows"
                                    :per-page="perPage"
                                    aria-controls="my-table"
                            ></b-pagination>
                        </div>
                    </div>

                </b-tab>
                <b-tab title="实时财经消息"><p>I'm the second tab</p></b-tab>
                <b-tab title="数据分析知识"><p>I'm a disabled tab!</p></b-tab>
            </b-tabs>

        </div>

    </div>

</template>
<style>
    .w-100 {
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
    export default {
        data() {
            return {
                value: [],
                selected: null,
                week_options: ['正序'],
                perPage: 3,
                currentPage: 1,
                items: [
                    {JJDM: 1, GUIMO: 'Fred', WEEK: 'Flintstone', MONTH: '0', TWEEK: 2, HYEAR: 6, YEAR: 9},

                ]
            }
        },
        name: "JiJinList"
    }
</script>

