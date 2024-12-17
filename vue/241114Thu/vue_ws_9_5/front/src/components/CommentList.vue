<template>
  <li>
    <span class="comment-author">{{ comment.user.username }} | </span>
    <span class="comment-content">{{ comment.content }}</span>
    <button 
      v-if="comment.user.username === authStore.user.username"
      @click="commentDelete"
    >
      🗑
    </button>
  </li>
</template>

<script setup>
import { useCommentStore } from '../stores/comments';
import { useAuthStore } from '../stores/auth';
const authStore = useAuthStore()
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