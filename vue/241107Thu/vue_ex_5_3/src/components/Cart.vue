<template>
  <div>
    <h2>장바구니</h2>
    <ul>
      <li v-for="item in cartItems" :key="item.id">
        {{ item.name }} - {{ item.price }}원
        <button @click="removeFromCart(item.id)">삭제</button>
      </li>
    </ul>
    <p>총 가격: {{ totalPrice }}원</p>
  </div>
</template>

<script setup>
const { cartItems, totalPrice } = defineProps({
  cartItems: Array,
  totalPrice: Number
})

const emit = defineEmits(['remove-from-cart'])

function removeFromCart(productId) {
  emit('remove-from-cart', productId)
}
</script>
