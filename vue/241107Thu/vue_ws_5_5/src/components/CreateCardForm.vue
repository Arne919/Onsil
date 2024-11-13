<script setup>
import { ref } from 'vue'
import { defineEmits } from 'vue'
const name = ref("");
const title = ref("");
const emit = defineEmits(['createCardEvent'])
const createCardFunc = () => {

    const cardInfo = {
        name: name.value,
        title: title.value
    }
    emit('createCardEvent', cardInfo)
    name.value = "";
    title.value = "";
}

</script>
<template>
  <div class="form-container">
  <form>
      <label for="name" class="form-label">이름</label>
      <input type="text" class="form-input" id="name" v-model="name">
      <label for="title" class="form-label">직함</label>
      <input type="text" class="form-input" id="title" v-model="title">
      <button class="new-card-btn" @click.prevent="createCardFunc">명함 추가</button>
  </form>
  </div>

</template>

<style scoped>
.form-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 3vh;
}
.form-input{
    width: 300px;
    height: 30px;
    margin-bottom: 10px;
    border: 1px solid #007acc;
    border-radius: 5px;
    padding: 5px;
    font-size: 16px;
}
.form-label{
    font-size: 16px;
    font-weight: bold;
    margin: 5px 15px;
}
.new-card-btn{

    margin-left: 15px;
    padding: 10px;
    border: 1px solid #007acc;
    border-radius: 5px;
    background-color: white;
    color: #007acc;
    font-size: 16px;
    cursor: pointer;
}
.new-card-btn:hover{
    background-color: #007acc;
    color: white;
}
</style>