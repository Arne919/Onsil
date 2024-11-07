<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름: {{ child.name }}</p>
    <p>나이: {{ child.age }}</p>
    <p>용돈: {{ child.balance }}원</p>
    <button @click="requestAllowance">용돈 주세요.</button>
  </div>
</template>

<script setup>
const { child } = defineProps({
  child: Object,
})
const emit = defineEmits(['giveMeAllowance'])
function requestAllowance() {
  emit('giveMeAllowance')
}
</script>

<style scoped>

</style>