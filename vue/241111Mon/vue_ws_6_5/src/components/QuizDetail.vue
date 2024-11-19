<template>
  <div class="quiz-item">
    <h5 class="quiz-question">{{ quiz.pk }}번 문제. {{ quiz.question }}</h5>
    <label class="answer-label" :for="'answer' + quiz.pk">정답 입력</label>
    <input 
      type="text" 
      :id="'answer' + quiz.pk" 
      class="answer-input"
      v-model="userAnswer"
      @keyup.enter="submitAnswer(quiz)"
    >
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue';


defineProps({
  quiz: Object
})

const router = useRouter()
const submitAnswer = (quiz) => {
  const answer = window.confirm(`${userAnswer.value} 을/를 답안으로 제출합니다. 확실합니까?`)
  if (answer) {
    router.push(
      {
        name: 'answer', 
        params:
          { 
            pk: quiz.pk, 
            answer: quiz.answer
          }, 
        query: 
          {
            userAnswer: userAnswer.value 
          }
      })
  } else {
    userAnswer.value = ''
  }
}

const userAnswer = ref('');

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