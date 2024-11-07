<template>
  <ul>
    <ProductListItem 
      v-for="product in products" 
      :key="product.id" 
      :product="product"
      @add-to-cart="handleAddToCart"
    />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'

const { products } = defineProps({
  products: Array
})

const emit = defineEmits(['add-to-cart'])

function handleAddToCart(product) {
  emit('add-to-cart', product) // App.vue로 이벤트 전달
}
</script>
