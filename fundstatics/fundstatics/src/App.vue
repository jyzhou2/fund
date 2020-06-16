<template>
  <div id="app">
   <el-container>
    <el-header>
      <div>
  <el-link  type="primary">主题基金</el-link>
  <el-link   type="success">涨幅排名</el-link>
  <el-link  type="warning">跌幅排名</el-link>
  <el-link    type="danger">稳定性排名</el-link>
  <el-link type="info">综合排名</el-link>
</div>
    </el-header>
    <el-main>Main</el-main>
   </el-container>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.el-header{
  color:white;
}

  .el-header, .el-footer {


    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
   # background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  .el-link{
    width: 200px;
  }



  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

</style>
