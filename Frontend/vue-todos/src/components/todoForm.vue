<template>
  <el-form @submit.prevent :inline="true" :model="formImput" class="todo-form-input">
    <el-form-item label="Title" prop="title">
      <el-input v-model="formInput.title" placeholder="enter todo"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit()">Add</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts">
import { ElMessage} from 'element-plus';
import { Options, Vue } from 'vue-class-component';

@Options({})
export default class TodoForm extends Vue{
    formInput = { title: "", complated: false };

    onSubmit(){
      if(this.formInput.title.length > 3) {

        this.$emit('send-message', this.formInput);
      } else {
          ElMessage({
            message: "Warning, this is to short",
            type: "warning"


          
          })
      }
      this.formInput.title = "";

    }
    
}
</script>