<template>
  <div class="auth-form-container">
    <form @submit.prevent="handleFormSubmit">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" v-model="username">
      <br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" v-model="password">
      <br>
      <div v-if="isSignUpRoute">
        <label for="password2">Confirm Password:</label>
        <input type="password" id="password2" name="password2" v-model="password2">
      </div>
      <button class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useRoute } from 'vue-router';

const route = useRoute();
const store = useAuthStore();

const username = ref('');
const password = ref('');
const password2 = ref('');

const isSignUpRoute = route.name === 'signup';

const handleFormSubmit = () => {
  if (isSignUpRoute) {
    store.signUp(username.value, password.value, password2.value);
  } else {
    store.logIn(username.value, password.value);
  }
};
</script>

<style scoped>
.auth-form-container {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

label {
  font-weight: bold;
}

input {
  width: calc(100% - 16px);
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button.submit-button {
  background-color: #007bff;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button.submit-button:hover {
  background-color: #0056b3;
}
</style>
