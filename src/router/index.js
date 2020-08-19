import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/dashboard/Dashboard'
import CommentPage from '@/components/commentpage/CommentPage'
import indexCM from '@/components/commonpage/indexCM'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },    
    {
      path: '/comment',
      name: 'Comment',
      component: CommentPage
    },
    {
      path: '/common',
      name: 'indexCM',
      component: indexCM
    }
  ]
})
