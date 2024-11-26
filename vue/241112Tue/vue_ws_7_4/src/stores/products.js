import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductListStore = defineStore('productList', () => {
  const productList = ref([
    {
      name: '상품 1',
      imagePath: 'src/assets/product1.png',
      price: 10000,
      isFavorite: false
    },
    {
      name: '상품 2',
      imagePath: 'src/assets/product2.png',
      price: 20000,
      isFavorite: false
    },
    {
      name: '상품 3',
      imagePath: 'src/assets/product3.png',
      price: 30000,
      isFavorite: false
    },
    {
      name: '상품 4',
      imagePath: 'src/assets/product4.png',
      price: 40000,
      isFavorite: false
    },
  ])

  const updateIsFavorite = function (name) {
    productList.value = productList.value.map((product) => {
      if (product.name === name) {
        product.isFavorite = !product.isFavorite
      }
      return product
    })
  }

  const isFavoriteList = computed (() => {
    return productList.value.filter((product) => product.isFavorite)
  })
  return { productList, updateIsFavorite, isFavoriteList }
})
