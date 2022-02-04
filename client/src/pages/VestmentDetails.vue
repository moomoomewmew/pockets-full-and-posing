<template>
  <div class="vestment-content" >
    <section class="image-container">
      <div>
        <img :src="vestment.image" :alt="vestment.name" />
        
        </div>
    </section>
    <section class="details">
      <div class="flex-row space"></div>
      <div>
        <h3>{{ vestment.name }}</h3>
        <p> {{ vestment.description }}</p>
        <h4>{{ vestment.price }}</h4>
        <h4>{{ vestment.size }}</h4>
        <h4>{{ vestment.quantity }}</h4>
        <button @click="buyVestment(vestment.id)">Purchase</button>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
  
export default {
  name: 'VestmentDetails',
  data: () => ({
    vestment: null
  }),
  mounted: async function() {
    await this.getVestmentDetails()
  },
  methods: {
    async getVestmentDetails() {
      const vestmentId = parseInt(this.$route.params.vestment_id)
      const res = await axios.get(`http://localhost:8000/items/${vestmentId}`)
      this.vestment = res.data
    },
    async buyVestment(vestmentId) {
      await axios.put(`http://localhost:8000/items/${vestmentId}`, {
        quantity: this.vestment.quantity -= 1
      }, {
        headers: {
          username: 'benjaminobambino',
          password: 'pockets'
        }
      })
      .then(() => {
        this.getVestmentDetails()
      })
    }
  }
}

</script>