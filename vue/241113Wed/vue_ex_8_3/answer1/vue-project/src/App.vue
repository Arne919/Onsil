<template>
  <header>
    <nav>
      <RouterLink to="/">할 일 목록</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style scoped>
</style>
