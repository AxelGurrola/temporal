<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const email = ref('');
const password = ref('');

const register = async () => {
  const res = await axios.post('http://localhost:3000/register', {
    email: email.value,
    password: password.value
  });
  alert(res.data.message);
};
</script>
