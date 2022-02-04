<template>
<div class ="vestment-card">
  <div class="-image-wrapper">
    <img :src="vestment.image" />
  </div>
  <div class="info-wrapper">
    <h3>{{ vestment.name }}</h3>
    <h4>Price: ${{ vestment.price }}</h4>
  </div>
</div>
</template>

<script>
export default {
  name: 'VestmentCard',
  props: ['vestment']
}
</script>