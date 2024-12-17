import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import PostListView from '@/views/PostListView.vue'
import PostDetailView from '@/views/PostDetailView.vue'
import CategoryCreateView from '@/views/CategoryCreateView.vue'
import PostFormView from '@/views/PostFormView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import { useAuthStore } from '../stores/auth.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/posts',
      name: 'posts',
      component: PostListView
    },
    {
      path: '/detail/:pk',
      name: 'detail',
      component: PostDetailView
    },
    {
      path: '/category',
      name: 'category',
      component: CategoryCreateView,
      beforeEnter: (to, from) => {
        const store = useAuthStore()
        if (!store.user.is_superuser) {
          return { name: 'main' }
        }
      }
    },
    {
      path: '/post',
      name: 'postCreate',
      component: PostFormView
    },
    {
      path: '/post/:pk',
      name: 'postUpdate',
      component: PostFormView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: (to, from) => {
        const store = useAuthStore()
        if (store.isAuthenticated) {
          return { name: 'main' }
        }
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView,
      beforeEnter: (to, from) => {
        const store = useAuthStore()
        if (store.isAuthenticated) {
          return { name: 'main' }
        }
      }
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useAuthStore()
  if (to.name != 'login' && to.name != 'signup' && !store.isAuthenticated ) {
    return { name: 'login' }
  }
})

export default router
