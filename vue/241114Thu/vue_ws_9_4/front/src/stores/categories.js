import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from './auth'
import { useRouter } from 'vue-router'

export const useCategoryStore = defineStore('category', () => {
  const token = useAuthStore().token
  const router = useRouter()
  const categoryList = ref([])
  const getCategoryList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/category/',
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => categoryList.value = res.data)
    .catch(err => console.log(err))
  }

  const createCategory = function (name) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/category/',
      data: {
        name: name
      },
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => {router.push({name: 'main'})})
  }
  return { categoryList, getCategoryList, createCategory, token }
}
)
