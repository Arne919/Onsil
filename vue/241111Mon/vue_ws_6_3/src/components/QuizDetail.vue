<template>
  <div class="quiz-item">
    <h5 class="quiz-question">{{ quiz.pk }}번 문제. {{ quiz.question }}</h5>
    <label class="answer-label" :for="'answer' + quiz.pk">정답 입력</label>
    <input type="text" :id="'answer' + quiz.pk" class="answer-input">
  </div>
</template>

<script setup>
defineProps({
  quiz: Object
})

</script>

<style  scoped>

.quiz-item {
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  margin: 20px 0;
  background-color: #f9f9f9;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.1);
}

.quiz-question {
  font-size: 18px;
  margin: 0;
}

.answer-label {
  display: block;
  font-size: 16px;
  margin-top: 15px;
}

.answer-input {
  width: calc(100% - 24px);
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  margin-top: 8px;
}

</style>