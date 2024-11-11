<template>
  <div>
    <h1>User Profile</h1>
    <p>Username: {{ username }}</p>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  username: String
})
</script>

<style scoped>
</style>