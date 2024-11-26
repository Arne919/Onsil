<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useProductListStore } from './stores/products';
const store = useProductListStore()
</script>

<template>
  <div>
    <header class="header">
      <div class="wrapper">
        <nav class="nav">
          <RouterLink to="/" class="nav-link">Home</RouterLink>
          <RouterLink to="/products" class="nav-link">Products</RouterLink>
          <RouterLink to="/favorite" class="nav-link">
            Favorite
            <span class="favorite-count" v-if="store.isFavoriteList.length">
              {{ store.isFavoriteList.length }}
            </span>
          </RouterLink>
        </nav>
      </div>
    </header>

    <main class="main">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.header {
  background-color: #333;
  color: white;
  padding: 10px 0;
}

.wrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.nav {
  display: flex;
  justify-content: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  margin: 0 15px;
  font-size: 18px;
}

.main {
  padding: 20px;
}

.favorite-count {
  background-color: red;
  color: white;
  border-radius: 50%;
  padding: 4px 8px;
  margin-left: 4px;
  font-size: 12px;
}
</style>
