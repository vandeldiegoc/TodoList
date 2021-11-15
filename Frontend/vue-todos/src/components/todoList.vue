<template>
  <el-row>
    <el-col :span="12" :offset="7" style="width: 100%">
      <h1>todoList</h1>
      <todo-form @send-message="createTodo"></todo-form>
      <el-table :data="todos">
        <el-table-column prop="title" label="Title"/>
        <el-table-column prop="complated" label="Completed"/>
      </el-table>
    </el-col>
  </el-row>
</template>

<script lang="ts">
import { ElMessage } from "element-plus";
import { Options, Vue } from "vue-class-component";
import TodoForm from "./todoForm.vue";

@Options({
  components: {
    TodoForm,
  },
})
export default class todoList extends Vue {
  todos = [];

  async mounted() {
    await this.loadTodo();
  }
  async loadTodo() {
    const response = await this.axios.get("http://localhost:8001/todos");
    this.todos = response.data;
    console.log(this.todos)
  }
  // eslint-disable-next-line
  async createTodo(todo : any) {
    console.log("Todo", todo);
    await this.axios.post("http://localhost:8001/create", {
      title: todo.title,
      complated: todo.completed
    })


    ElMessage({
      message: "todo created",
      type: "success",
    });
    await this.loadTodo()
  }


  // eslint-disable-next-line
  async updateTodo(todo : any) {
    console.log("Todo", todo);
    await this.axios.put(`http://localhost:8001/create/${todo.id}`, {
      id = todo.id,
      title: todo.title,
      complated: todo.completed
}
</script>