<template>
<div class ="vestment-card">
  <div class="-image-wrapper">
  <!-- <img :src="this.vestment.image" /> -->
  </div>
  <div class="info-wrapper">
    <!-- {{ vestment.name }} -->
  </div>
  <div>
    <!-- Price {{ vestment.price }} -->
  </div>
</div>
</template>

<script>
export default {
  name: 'Vestment Card',
  props: {
    vestment: {
      name: "",
      price:{}

    }},
    methods: {
      // selectVestment(vestmentId){
      //   this.$emit('selectVestment', vestmentId)
      }
    }
// }
</script>