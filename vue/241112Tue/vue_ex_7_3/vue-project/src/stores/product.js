import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  const products = ref([])

  const fetchProducts = function () {
    // case 1
    axios({
      method: 'get',
      url: 'https://jsonplaceholder.typicode.com/posts'
    })
    // case 2
    // return axios({
    //   method: 'get',
    //   url: 'https://jsonplaceholder.typicode.com/posts'
    // })
      .then(response => {
        products.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const productCount = computed(() => products.value.length)

  const deleteProduct = function (productId) {
    // 요소를 직접 수정하는 대신에 splice 메서드를 사용하여 새로운 배열을 생성하여 상태를 업데이트
    const index = products.value.findIndex(product => product.id === productId)
    if (index !== -1) {
      products.value.splice(index, 1)
    }
  }

  // 수정은 문제 보강이 필요할 경우 사용
  // const editProduct = function (productId, editedProduct) {
  //   const index = products.value.findIndex(product => product.id === productId)
  //   if (index !== -1) {
  //     products.value[index] = editedProduct
  //   }
  // }

  return { products, productCount, fetchProducts, deleteProduct }
  // return { products, productCount, fetchProducts, deleteProduct, editProduct }
})
