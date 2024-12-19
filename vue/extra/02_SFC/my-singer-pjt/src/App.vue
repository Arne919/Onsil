<template>
  <!-- 2. 불러온 객체 MainPage를 화면에 보여준다. -->
   <MainPage />
   <SingerList />
</template>

<script setup>
// 1. 내가 만들어둔 MainPage 뷰 객체를 import 한다.
import MainPage from './components/MainPage.vue';
import SingerList from './components/SingerList.vue';
</script>

<style scoped>
</style>
