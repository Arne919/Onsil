<template>
  <div>
    <h2>Product List</h2>
    <ul>
      <!-- case 1 -->
      <ProductListItem 
        v-for="product in store.products" 
        :key="product.id" 
        :product="product" 
      />
      <!-- case 2 -->
      <!-- <ProductListItem 
        v-for="product in products" 
        :key="product.id" 
        :product="product" 
      /> -->
    </ul>
  </div>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'
import { useProductStore } from '@/stores/product'
import { ref, onMounted } from 'vue'

const store = useProductStore()

// case 1
onMounted(() => {
  store.fetchProducts()
  // .then(() => {
    //   products.value = store.products
    // })
  })
  

// case 2

// const products = ref([])

// onMounted(() => {
//   store.fetchProducts()
//     .then(() => {
//       products.value = store.products
//     })
// })
</script>
