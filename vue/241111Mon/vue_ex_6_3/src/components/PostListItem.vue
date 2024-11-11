<template>
  <li>
    <RouterLink :to="{ name: 'post-detail', params: { username, id: post.id } }">
      {{ post.title }}
    </RouterLink>
  </li>
</template>

<script setup>
import { defineProps } from 'vue'
import { useRoute } from 'vue-router'

const props = defineProps({
  post: Object
})

const route = useRoute()
const username = route.params.username
</script>
