import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '/src/views/HomeView.vue';
import QuizView from '/src/views/QuizView.vue';
import AnswerView from '/src/views/AnswerView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/quiz',
      name: 'quiz',
      component: QuizView,
    },
    {
      path: '/answer/:pk/:answer',
      name: 'answer',
      component: AnswerView,
      beforeEnter: (to, from) => {
        setTimeout(() => {
          router.push({name: 'quiz'})
        }, 4000)
        
      }
    },
  ]
})

export default router
