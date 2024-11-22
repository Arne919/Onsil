<template>
  <li>
    {{ product.id }} - {{ product.title }} - {{ product.body }}
    <button @click="deleteProduct(product.id)">Delete</button>
    <!-- <button @click="editProduct(product.id)">Edit</button> -->
  </li>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

defineProps({
  product: Object
})

const store = useProductStore()

const deleteProduct = function (productId) {
  store.deleteProduct(productId)
}

// const editProduct = function (productId) {
//   const editProduct = {
//     id: productId,
//     title: 'Edited Product',
//     body: 'New Description'
//   }
//   store.editProduct(id, editProduct)
// }
</script>

<style scoped>

</style>
