import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from './auth'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const router = useRouter()
  const store = useAuthStore()

  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then(res => {
      router.push({ name: 'home' })
    })
  }

  return { articles, getArticles, createArticle }
})
