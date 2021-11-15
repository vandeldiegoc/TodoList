<template>
  <el-container>
    <el-main>
      <todo-list></todo-list>
    </el-main>
  </el-container>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import todoList from './components/todoList.vue'

@Options({
  components: {
    todoList,
  },
})
export default class App extends Vue {}
</script>

<style>
body{
  margin: 0;
}

.el-container{
  background-color: #e9eef9;
  color: var(--el-text-color-primary);
  text-align: center;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
