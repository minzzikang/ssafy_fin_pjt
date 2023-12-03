import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/Movies/HomeView.vue'
import SignUpView from '@/views/Accounts/SignUpView.vue'
import RecommendView from '@/views/Movies/RecommendView.vue'
import SearchView from '@/views/Movies/SearchView.vue'
import MovieDetailView from '@/views/Movies/MovieDetailView.vue'
import ArticleCreateView from '@/views/Articles/ArticleCreateView.vue'
import ArticleView from '@/views/Articles/ArticleView.vue'
import ArticleDetailView from '@/views/Articles/ArticleDetailView.vue'
import ArticleEditView from '@/views/Articles/ArticleEditView.vue'
import UserView from '@/views/Users/UserView.vue'
import UserUpdateView from '@/views/Users/UserUpdateView.vue'
import UserInfoUpdateView from '@/views/Users/UserInfoUpdateView.vue'
import { useMovieStore } from '@/stores/movie'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/mvti',
      name: 'recommend',
      component: RecommendView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: MovieDetailView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/article/:id',
      name: 'articleDetail',
      component: ArticleDetailView
    },
    {
      path: '/article/edit/:id',
      name: 'articleEdit',
      component: ArticleEditView
    },
    {
      path: '/user',
      name: 'user',
      component: UserView
    },
    {
      path: '/user/update',
      name: 'userUpdate',
      component: UserUpdateView
    },
    {
      path: '/user/infoupdate',
      name: 'userInfoUpdate',
      component: UserInfoUpdateView
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useMovieStore()
  if (to.name === 'recommend' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'home'}
  }
  // if ((to.name === 'signup' || to.name === 'home') && (store.isLogin)) {
  //   window.alert('이미 로그인 되었습니다.')
  //   return { name: 'recommend'}
  // }
})
export default router
