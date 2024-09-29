import { createMemoryHistory, createRouter } from 'vue-router'

import userDashView from '../views/userDashView.vue'
import landingView from '../views/landingView.vue'

const routes = [
  { path: '/', component: landingView },
  { path: '/user/dashboard', component: userDashView },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router
