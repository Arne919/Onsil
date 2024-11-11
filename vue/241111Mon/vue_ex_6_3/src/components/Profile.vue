<template>
  <div>
    <hr>
    <h2>상세 프로필</h2>
    <p>반갑습니다. {{ username }}입니다.</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const username = route.params.username
</script>

<style scoped>

</style>