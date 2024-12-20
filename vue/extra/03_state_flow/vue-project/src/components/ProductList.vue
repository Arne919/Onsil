<template>
  <!-- 하위 컴포넌트 들을 v-for를 사용해서 가지고 있는 데이터 수만큼 렌더링 -->
  <!-- 최상위 요소 하나 만들어주기 // CSS도 생각해서 적절한 class 부여 -->
  <ul class="product-list">
    <!-- productitem 컴포넌트들 -->
     <!-- 하위 컴포넌트에서 어떤 이벤트가 발생하면 특정 함수를 실행!!! -->
      <!-- v-on (단, html은 대소문자 구분이 안되서 cebob-case) -->
     <ProductItem 
      v-for="product in products"
      :key="product.id"
      :product="product"
      @add-to-cart="addToCart(product)"
     />
     <!-- <p>{{ products }}</p> -->
  </ul>
</template>

<script setup>
  import ProductItem from './ProductItem.vue'
  defineProps({
    products: Array
  })
  const emit = defineEmits(['addToCart'])
  // 만약 1, 2번째 방법으로 넘겨받은 인자가 있다면, 그곳에 들어있는 데이터가 무엇인지 확인해야한다.
  const addToCart = function (item) {
    emit('addToCart', item)
  }
</script>

<style scoped>

</style>