<template>
  <div>
    <h1>User Profile</h1>
    <p>Username: {{ username }}</p>
    <nav>
      <RouterLink :to="{ name: 'user-profile', params: { username } }">상세 프로필</RouterLink> |
      <RouterLink :to="{ name: 'user-posts', params: { username } }">작성한 게시글</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)
</script>
