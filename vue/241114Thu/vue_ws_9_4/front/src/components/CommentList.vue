<template>
  <li>
    <span class="comment-author">{{ comment.user.username }} | </span>
    <span class="comment-content">{{ comment.content }}</span>
    <button @click="commentDelete">🗑</button>
  </li>
</template>

<script setup>
import { useCommentStore } from '../stores/comments';
const store = useCommentStore()
const props = defineProps({
  comment: Object
})

const commentDelete = () => {
  store.commentDelete(props.comment.post, props.comment.id)
}
</script>

<style lang="scss" scoped>

</style>