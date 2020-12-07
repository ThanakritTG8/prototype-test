import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Patong/dashboard/Dashboard'
import CommentPage from '@/components/Patong/commentpage/CommentPage'
import indexCM from '@/components/Patong/commonpage/indexCM'
import indexCMkaron from '@/components/Karon/commonpage/indexCMkaron'
import DashboardKaron from '@/components/Karon/dashboard/DashboardKaron'
import IndexRelated from '@/components/Patong/relatedword/IndexRelated'
import IndexRelatedKaron from '@/components/Karon/relatedword/IndexRelatedKaron'
import CommentPageKaron from '@/components/Karon/commentpage/CommentPageKaron'
import Home from '@/components/Home'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/dashboard',
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
      path: '/common/karon',
      name: 'indexCMkaron',
      component: indexCMkaron
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
    ,
    {
      path: '/related/karon',
      name: 'IndexRelatedKaron',
      component: IndexRelatedKaron
    }
    ,{
      path: '/Comment/karon',
      name: 'CommentPageKaron',
      component: CommentPageKaron
    }
  ]
})
