<template>
  <header>
    <nav v-if="userStore.isLogin" >
      <RouterLink to="/">할 일 목록</RouterLink>
      <RouterLink to="/todo/create">할 일 등록</RouterLink>
    </nav>
    <nav v-else>
      <RouterLink to="/">할 일 목록</RouterLink>
      <RouterLink to="/signup">회원가입</RouterLink>
      <RouterLink to="/login">로그인</RouterLink>

    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
import { useUserStore } from "@/stores/userStore.js";

const userStore = useUserStore();
</script>

<style scoped>
nav a {
  margin-right: 10px;
}
</style>
