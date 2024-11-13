<template>
  <div>
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage
      v-for="child in family.children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';
defineProps({
  family: Object
})
</script>

<style scoped>
  /* 전체 컨테이너 스타일 */
  div {
    border: 1px solid #ccc;
    padding: 20px;
    margin: 20px;
    background-color: #f9f9f9;
    text-align: center;
  }

  /* 제목 스타일 */
  h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }

  /* 부모/자식 정보 스타일 */
  p {
    font-size: 18px;
    margin: 5px;
  }

  /* ChildPage 컴포넌트 스타일 */
  .child-container {
    border: 1px solid #ddd;
    padding: 10px;
    margin: 10px;
    background-color: #fff;
  }
</style>