<template>
<div class ="vestment-card">
  <div class="-image-wrapper">
    <img :src="vestment.image" />
  </div>
  <div class="info-wrapper">
    <h3>{{ vestment.name }}</h3>
    <h4>Price: ${{ vestment.price }}</h4>
    <h4>Department: {{ department }}</h4>
    <h5>Quantity: {{ vestment.quantity }}</h5>
    <h5>Size: {{ vestment.size }}</h5>
    <p>{{ vestment.description }}</p>
  </div>
</div>
</template>

<script>
export default {
  name: 'VestmentCard',
  props: ['vestment', 'department']
}
</script>