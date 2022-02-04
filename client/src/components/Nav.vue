<template>
<header>
  <span class="material-icons">
shopping_cart
</span>
  <nav >
    <router-link class="nav" to="/">Home</router-link>
    <router-link class="nav" to="/vestments">Vestments</router-link>
    <router-link class="nav" to="/about">About</router-link>
  </nav>
</header>
</template>

<script>
export default {
  name: 'Nav'
}
</script>

<style scoped></style>