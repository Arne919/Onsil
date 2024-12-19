<!-- 
  index.html에 직접 mount 하지 않음. 
  하나의 프로젝트에서 index.html에 마운트되는 vue 객체는
  오라지 App.vue 하나!
-->
<template>
  <div class="main">
    <h1>Welcome to Singer Info Page</h1>
    <p>Find your favorite Singer and artist</p>
    <!-- 
      경로 -> 상대 경로. 
      vue의 상대경로는 아주 심플하다. 왜냐?
      모든 내가 직접 작성하거나 관리해야하는 내용물들은
      root/src/ 안에 있다. -> 그럼 루트경로/src? 매번쓰겠네?
      vite.config.js 이파일에 vue가 alias 만들어 뒀다.
    -->
    <img 
      src="@/assets/microphone.jpg" 
      alt="microphone"
      width="200px"
    >
  </div>
</template>

<script setup>

</script>

<style scoped>
.main {
  /* CSS 레이아웃 영역 지정하기 어렵다면 일단 background-color를 먹이자 */
  /* background-color: red; */
  width: 1200px;
  margin: auto;
  text-align: center;
}

</style>