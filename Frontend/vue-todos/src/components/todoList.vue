<template>
  <el-row>
    <el-col :span="12" :offset="7" style="width: 100%">
      <h1>todoList</h1>
      <todo-form @send-message="createTodo"></todo-form>
      <el-table :data="todos">
        <el-table-column prop="title" label="Title" width="350" />
        <el-table-column fixed="right" label="Operations" width="200">
          <template #default="scope">
            <el-space wrap>
              <el-switch
                v-model="scope.row.complated"
                @click="updateTodo(scope.row)"
                />
              <el-popconfirm 
                confirm-button-text="Yes"
                cancel-button-text="No"
                icon="el-icon-info"
                icom-color="red"
                title="Are you sure you want todelete this?"
                @confirm="handleDelete(scope.row)"
                @cancel="cancelDelete">
                <template #reference>
                  <el-button
                    size="mini"
                    type="danger">
                    Delete
                  </el-button>  
                </template>
              </el-popconfirm>
              </el-space>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
  </el-row>
</template>

<script lang="ts">
import { ElMessage } from "element-plus";
import { Options, Vue } from "vue-class-component";
import TodoForm from "./todoForm.vue";

interface Todo {
  id: number
  title: string
  complated: boolean
}

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
      complated: todo.complated
    })


    ElMessage({
      message: "todo created",
      type: "success",
    });
    await this.loadTodo()
  }


  // eslint-disable-next-line
  async updateTodo(todo : Todo) {
    console.log("Todo", todo);
    await this.axios.put(`http://localhost:8001/create/${todo.id}`, {
      id: todo.id,
      title: todo.title,
      complated: todo.complated
    })

    ElMessage({
      type: "success",
      message: "todo updated",
    });
    await this.loadTodo()
  }
  async handleDelete(todo: Todo) {
    await this.axios.delete(`http://localhost:8001/delete/${todo.id}`)
    ElMessage({
      type: "success",
      message: "todo updated",
    });
    await this.loadTodo()

  }
  cancelDelete(){
    console.log("canceled the delete")
  }
}
</script>