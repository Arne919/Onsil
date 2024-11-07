<template>
  <li>
    {{ product.name }} - {{ product.price }}원
    <button @click="addToCart">장바구니에 추가</button>
  </li>
</template>

<script setup>
const { product } = defineProps({
  product: Object
})

const emit = defineEmits(['add-to-cart'])

function addToCart() {
  emit('add-to-cart', product) // product 객체를 emit
}
</script>
