<template>
  <div class="singer-list">
    <h1>Singer List</h1>
    <!-- 아래 요소를 내가 가지고 있는 data 수만큼 v-for로 반복 -->
    <!-- 
      이렇게 만든 card 모양의 template을 
      만약, singerlist 말고 다른곳에서도 쓸 수 있다면?
      MainPage 말고도, 다른 곳에서도 쓸 수 있다면?
      -> 별도의 component로 다루는게 좋겠다.
    -->
    <!-- <div class="card">
      <h1>name</h1>
      <img src="" alt="">
      <p>descript</p>
    </div> -->
    <!-- 
      레이아웃이 내가 생각한거랑 다른 상황이 되었다? 
      그때 달라진 부분을 보완하면 된다.
    -->
    <div class="card-list">
      <!-- 어떤 요소가 vue가 가진 데이터를 사용할 수 있도록 하는법 -> binding -->
      <SingerCard   
        v-for="card in [{name: 'adele'}, {name: 'iu'}, {name: 'bruno'}, {name: 'roze'}]"
        :key="card"
        :card="card"
      />
    </div>
  </div>
</template>

<script setup>
import SingerCard from './SingerCard.vue';
</script>

<style scoped>
  .singer-list {
    padding: 10px;
    /* background-color: slategray; */
    text-align: center;
  }

  .singer-list h1 {
    margin:  0px;
  }

  .card-list {
    /* background-color: blue; */
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }
</style>