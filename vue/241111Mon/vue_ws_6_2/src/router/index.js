import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '/src/views/HomeView.vue';
import QuizView from '/src/views/QuizView.vue';


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
  ]
})

export default router
