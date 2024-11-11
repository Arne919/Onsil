<template>
  <div>
    <h2>{{ username }}님의 작성한 게시글</h2>
    <ol>
      <PostListItem
        v-for="post in posts"
        :key="post.id"
        :post="post"
      />
    </ol>
    <RouterView />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import PostListItem from './PostListItem.vue'

const route = useRoute()
const username = route.params.username
const posts = [
  { id: 1, title: '제목: Post 1', content: '첫 번째 게시글의 내용' },
  { id: 2, title: '제목: Post 2', content: '두 번째 게시글의 내용' },
  { id: 3, title: '제목: Post 3', content: '세 번째 게시글의 내용' },
]
</script>
