import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Patong/dashboard/Dashboard'
import CommentPage from '@/components/Patong/commentpage/CommentPage'
import indexCM from '@/components/Patong/commonpage/indexCM'
import DashboardKaron from '@/components/dashboardKaron/DashboardKaron'
import IndexRelated from '@/components/relatedword/IndexRelated'
import Home from '@/components/Home'


Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'Home',
    //   component: Home
    // },
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
    },
    {
      path: '/dashboard/karon',
      name: 'DashboardKaron',
      component: DashboardKaron
    },
    {
      path: '/related',
      name: 'IndexRelated',
      component: IndexRelated
    }
  ]
})
