<template>
  <div>
    <p>이름: {{ info.name }}</p>
    <p>잔고: {{ info.balance }}</p>
    <button class="update-button" @click="updateRoute">updateBalance</button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({
  info: Object
})

const updateRoute = () => {
  router.push({name:'update', params:{name: props.info.name}})
}

</script>

<style scoped>
.update-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 4px;
}

.update-button:hover {
  background-color: #0056b3;
}
</style>
