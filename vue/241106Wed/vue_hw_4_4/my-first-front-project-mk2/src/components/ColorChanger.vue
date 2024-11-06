<template>
    <div>
        <input v-model="colorClass" placeholder="red, blue, green 입력하시오." />
        <p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
      
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        colorClass: ''
      }
    }
  }
  </script>
  
  <style>
  .red {
    color: red;
  }
  .blue {
    color: blue;
  }
  .green {
    color: green;
  }
  </style>
  