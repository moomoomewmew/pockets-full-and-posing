import VueRouter from 'vue-router';
// import components
import Home from './pages/Home';
import ViewVestments from './pages/ViewVestments';
import VestmentDetails from './pages/VestmentDetails';
// import About from './pages/About';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  // { path: '/about', component: About, name: 'About' },
  {
    path: '/details/:vestment_id',
    component: VestmentDetails,
    name: 'VestmentDetails'
  },
  {
    path: '/vestments-by-department/:department_id/:department_name',
    component: ViewVestments,
    name: 'ViewVestments'
  }
];

export default new VueRouter({
  routes,
  mode: 'history'
});
