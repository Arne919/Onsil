<script setup>
import { computed } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from './stores/auth';
const store = useAuthStore()
const isAuthenticated = computed(() => {
  return store.isAuthenticated
})


</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <span
          v-if="!isAuthenticated"
        >
          <RouterLink to="/signup">SignUp</RouterLink> | 
          <RouterLink to="/signin">SignIn</RouterLink> | 
      </span>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
