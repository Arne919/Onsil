<template>
  <div>
    <form 
      @submit.prevent="route.name === 'signup'? store.signUp(username, password, password2) : store.logIn(username, password)"
    >
      <label for="username">username : </label>
      <input type="text" id="username" name="username" v-model="username"> <br>
      <label for="password">password : </label>
      <input type="password" id="password" name="password" v-model="password"><br>
      <div
        v-if="route.name === 'signup'"
      >
        <label for="password2">password Confirmation : </label>
        <input type="password" id="password2" name="password2" v-model="password2"><br>
      </div>
      <button>submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth.js'
import { useRoute } from 'vue-router';

const route = useRoute()
const store = useAuthStore()

const username = ref('')
const password = ref('')
const password2 = ref('')


</script>

<style lang="scss" scoped>

</style>