<script setup>
import { computed } from 'vue'
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
        <span
        v-if="!isAuthenticated"
        >
        <RouterLink to="/signup">SignUp</RouterLink> 
        <RouterLink to="/login">LogIn</RouterLink>
      </span>
      <span v-else>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink :to="{name: 'posts'}">PostList</RouterLink>
        <span v-if="store.user.is_superuser">
          <RouterLink :to="{name: 'category'}">CategoryCreate</RouterLink>
        </span>
      </span>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

nav {
  display: flex;
  justify-content: center;
  background-color: #333;
  padding: 1rem 0;
}

nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 1rem;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}
</style>
