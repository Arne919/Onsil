<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름: {{ detailInfo.name }}</p>
    <p>잔고: {{ detailInfo.balance }}</p>
    <button @click="store.updateBalance(route.params.name)">+</button>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useBalanceStore } from '@/stores/balance.js'
const route = useRoute()
const store = useBalanceStore()

const detailInfo = store.detailInfo(route.params.name)
const getDetailInfo = store.getDetailInfo(route.params.name)
</script>

<style lang="scss" scoped>

</style>