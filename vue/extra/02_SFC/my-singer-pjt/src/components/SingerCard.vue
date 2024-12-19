<template>
  <div class="card">
    <h1>{{ card.name }}</h1>
    <img 
      src="@/assets/singer.jpg" 
      alt="singer"
      width="100px"
    >
    <p>descript</p>
  </div>
</template>

<script setup>
defineProps({
  card: Object
})
</script>

<style scoped>
.card {
  /* background-color: red; */
  margin: 20px 0px;
  width: 400px;
  border: 2px solid black;
}
</style>