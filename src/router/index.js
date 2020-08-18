import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/dashboard/Dashboard'
import CommentPage from '@/components/commentpage/CommentPage'
import CommonWordPage from '@/components/commonpage/CommonWordPage'

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
      name: 'Common',
      component: CommonWordPage
    }
  ]
})
