<template>
  <div class="quiz-create">
    <h2 class="create-title">퀴즈 생성</h2>
    <form class="quiz-form" @submit.prevent="createQuiz">
      <label for="question" class="form-label">문제</label>
      <textarea
        id="question"
        class="form-input"
        v-model="newQuiz.question"
        maxlength="200"
        rows="4"
        required
        @input="onChange"
      ></textarea>

      <label for="answer" class="form-label">답안</label>
      <input
        type="text"
        id="answer"
        class="form-input"
        v-model="newQuiz.answer"
        required
        @input="onChange"
      >

      <button type="submit" class="submit-button">퀴즈 생성</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const emit = defineEmits(['createQuiz', 'onChange'])

const newQuiz = ref({
  question: '',
  answer: ''
});

const createQuiz = () => {
  if (newQuiz.value.question && newQuiz.value.answer) {
    
    emit('createQuiz', newQuiz.value)
    newQuiz.value.question = '';
    newQuiz.value.answer = '';
  }
};

const onChange = () => {
  emit('onChange', newQuiz.value)
}

</script>

<style scoped>
.quiz-create {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.create-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.quiz-form {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-size: 16px;
  margin-top: 10px;
}

.form-input {
  resize: none;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
  margin-top: 5px;
}

.submit-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  margin-top: 15px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>
