<template>
  <div id="app">
    <header>
      <Nav />
    </header>
    <main>
      <router-view></router-view>
    </main>
    <footer>
      <Foot />
    </footer>
  </div>
</template>

<script>
import Foot from './components/Footer.vue'
import Nav from './components/Nav'

export default {
  name: 'App',
  components: {
    Nav,
    Foot
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
