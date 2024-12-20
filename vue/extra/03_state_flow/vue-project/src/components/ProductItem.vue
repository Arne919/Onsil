<template>
  <!-- 렌더링 할때는 prop 받은 데이터의 그 이름을 별도 처리 없이 그대로 사용 할 수 있다. -->
  <!-- 이건 vue가 처리해 주기 때문이다. -->
  <li class="product-item">
    {{ product.name }} - {{ product.price }} 원
    <!-- // 1번째 방법. addToCart 함수에 인자 방식으로 전달하기. -->
    <!-- <button @click="addToCart(product)">add to cart</button> -->
    <button @click="addToCart">add to cart</button>
  </li>
</template>

<script setup>
// prop 받을 데이터의 type도 정의 해주면 좋다.
// 넘겨받을 데이터의 type을 잘못 지정한다면, 무슨 일이 벌어지느냐?
// 넘겨받은 객체가 가지고 있지 않은 메서드 등에 접근하려고 하면 당연히 오류가 난다.
// props 객체가 가진 product 값을 변수 product에게 객체 구조 분해 할당 식으로 할당 가능.
  const { product } = defineProps({
    product: Object
  })
  // console.log(product)
  // 단, 이렇게 속성에 직접적으로 JS로 접근할 수 있다고 하더라도, 절대.
  // 하위컴포넌트에서 속성의 값을 수정하지 않는다.
  // 왜냐 -> 데이터의 흐름을 꺠트린다. 

  // 넘겨받은 데이터의 값에 따라 어떠한 로직이 필요할떄.
  // 장바구니에 추가하기 버튼을 눌렀을떄, 아무 상품이나 다 추가가 되는게 아니라,
  // 일정 금액 이하의 물건만 장바구니에 추가되도록 하고 싶다면?

  // 현재 product가 선택되었다는 사실을, 상위 컴포넌트에게 알려준다.
  // 즉, 현재 product가 선택되었다는 `이벤트`를 발생 시킨다.
  // 이벤트 -> click, input, submit 등등 외에 내가 직접 커스텀해서 마든 이벤트를 발생시킨다.
  const emit = defineEmits(['addToCart'])
  // const addToCart = function  (item) {
  const addToCart = function  () {
    // if (product.price >= 2000) {
    //   confirm(' 고가의 상품입니다. 장바구니에 담으시겠습니까? ')
    // }
    // addToCart 이벤트 발생!!! -> 어떻게 전파되느냐 (버블링)

    // 현재 컴포넌트가 가지고 있는 item이 무엇인지 상위컴포넌트에게 알릴 수 있는 방법
    // 1번째 방법. addToCart 함수에 인자 방식으로 전달하기.
    // 2번째 방법. props의 객체 값에서 필요한 속성을 변수에 할당후, 사용하기
    // emit('addToCart', product)

    // 3번째 방법. 나에게 prop 시켜준 부모 컴포넌트에게 맡기기.
    emit('addToCart')
  }
</script>

<style scoped>

</style>