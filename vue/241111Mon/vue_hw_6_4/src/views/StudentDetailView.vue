<template>
  <div>
    <h1>학생 상세 정보 페이지</h1>
    <p>{{ name }} 학생의 상세 정보입니다.</p>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  name: String, // 라우트에서 전달받은 name 파라미터를 props로 받아옵니다
})
</script>

<style scoped>

</style>