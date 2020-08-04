<template>
    <el-row class="tac">
  <el-col :span="12">
    <h5>默认颜色</h5>
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">基金筛选</span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">数据分析</span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">服务架构</span>
      </el-menu-item>
       <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">Laravel</span>
      </el-menu-item>
      </el-menu-item>
       <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">Python基础</span>
      </el-menu-item>
        <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">VUE</span>
      </el-menu-item>
        <!--
       <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span></span>
        </template>
        <el-menu-item-group>
          <template slot="title">分组一</template>
          <el-menu-item index="1-1">选项1</el-menu-item>
          <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="1-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <template slot="title">选项4</template>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      -->
    </el-menu>
  </el-col>
</el-row>

</template>
<script>
   export default {
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>