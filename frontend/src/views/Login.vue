<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const email = ref('');
const password = ref('');

const login = async () => {
  const res = await axios.post('http://localhost:3000/login', {
    email: email.value,
    password: password.value
  });
  alert(res.data.message);
};
</script>
