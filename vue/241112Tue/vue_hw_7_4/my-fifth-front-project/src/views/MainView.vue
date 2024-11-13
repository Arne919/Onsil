<template>
  <div class="main-container">
    <h1 class="main-title">메인 페이지</h1>
    <MainPage 
      v-for="info in store.balances"
      :key="info.name"
      :info="info"
    />
  </div>
</template>

<script setup>
import MainPage from '../components/MainPage.vue';
import { useBalanceStore } from '@/stores/balance.js'

const store = useBalanceStore()

const detailInfo = store.detailInfo('김서이')
const getDetailInfo = store.getDetailInfo('김서이')

</script>

<style scoped>
.main-container {
  padding: 20px;
}

.main-title {
  font-size: 24px;
  margin-bottom: 20px;
}
</style>
