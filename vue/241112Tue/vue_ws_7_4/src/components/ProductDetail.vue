<template>
  <div class="product-card">
    <h3 class="product-name">{{ product.name }}</h3>
    <img 
      :src="product.imagePath" 
      :alt="product.name"
      width="300"
    >
    <p class="product-price">₩ {{ product.price }}</p>
    <button 
      class="favorite-icon"
      @click="store.updateIsFavorite(product.name)"
    >
      <span v-if="product.isFavorite" role="img" style="color:red">❤</span>
      <span v-else role="img">🤍</span>
    </button>
  </div>
</template>

<script setup>
import { useProductListStore } from '@/stores/products.js'
const props = defineProps({
  product: Object
})

const store = useProductListStore()
</script>

<style scoped>
.product-card {
  border: 1px solid #ccc;
  padding: 20px;
  margin: 10px;
  text-align: center;
  width: 300px;
}

.product-name {
  font-size: 20px;
  margin-bottom: 10px;
}

.product-price {
  font-size: 18px;
  margin-bottom: 10px;
}

.favorite-icon {
  cursor: pointer;
  font-size: 24px;
  margin-top: 10px;
}

button {
  border: none;
  background: none;
  padding: 0;
  margin: 0;
  cursor: pointer;
}
</style>
