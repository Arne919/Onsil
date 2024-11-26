<template>
  <div class="product-list-page">
    <h1 class="page-title">상품 목록 페이지</h1>
    <div class="product-card-list">
      <ProductDetail 
        v-for="product in store.productList"
        :key="product.name"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import { useProductListStore } from '@/stores/products.js'
import ProductDetail from '../components/ProductDetail.vue';
const store = useProductListStore()
</script>

<style scoped>
.product-list-page {
  padding: 20px;
}

.page-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.product-card-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>
