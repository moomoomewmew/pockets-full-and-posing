import VueRouter from 'vue-router';
// import components
import Home from './pages/Home';

const routes = [{ path: '/', component: Home, name: 'Home' }];

export default new VueRouter({
  routes,
  mode: 'history'
});
