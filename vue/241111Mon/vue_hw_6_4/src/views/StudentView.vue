<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <ul>
      <li v-for="student in students" :key="student.name">
        <button @click="gotoStudentDetail(student.name)">{{ student.name }} 학생 정보 보기</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import {useRouter} from 'vue-router'
const students = [
  { name: '김하나'},
  { name: '김두리'},
  { name: '김서이'},
]
const router = useRouter()
function gotoStudentDetail(name) {
  router.push({ name: 'studentDetail', params: {name} })
  
}
</script>

<style scoped>

</style>