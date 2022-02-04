<template>
  <div class="vestment-content" >
    <section class="image-container">
      <div>
        <!-- <img/> -->
         <!-- {{ this.vestmentDetails.background }} -->
        
        </div>
    </section>
    <section class="details">
      <div class="flex-row space"></div>
      <div>
        <!-- <h3>{{ this.vestmentDetails.name }}</h3>
       <p> {{ this.vestmentDetails.description }}</p> -->
      </div>
    </section>
  </div>
</template>

<script>
// import axios from 'axios'
  
export default {
  
  name: 'VestmentDetails',
  data: () => ({
    vestmentDetails: {}
  }),
  mounted() {
    // this.getVestmentDetails()
  },
  methods: {
    async getVestmentDetails() {
     
      // Get vestment id from router here
    }
  }
}
</script>