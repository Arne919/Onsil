<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <!-- 왼쪽: 변수명 -->
     <!-- 오른쪽: 할당할 값 -->
    <ProductList 
      :products="products"
      @add-to-cart="addToCart"
    />

    <!-- <CartList 
      :cartlist="cartList"
    /> -->
  </div>
</template>

<script setup>
import { ref } from 'vue'
// 컴포넌트가 담기게 될 폴더명은 내가 직접 정해서 만들면된다.
// components/ 폴더안에도, 기능별로, 필요한 폴더를 더 만들어도 된다.
import ProductList from '@/components/ProductList.vue'
// import CartList from '@/components/CartList.vue'

const cartList = ref([])

// 이렇게, 하위 컴포넌트가 emit으로 넘긴 arg가, addToCart 함수를 호출할때 넣은 인자와 구분되도록
// 가능하면, 3번째 방식 (데이터의 주체가 가지고 있던 데이터를 활용)
const addToCart = function (data) {
  console.log('카트에 대상 추가.')
  console.log(data)
  cartList.value.push(data)
}

let id = 0
const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])
</script>
