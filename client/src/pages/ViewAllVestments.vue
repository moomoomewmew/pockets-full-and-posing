<template>
  <div class="view-departments">
    <h1>Vestments</h1>
    <section class="dropdown-menu">
      <label for="sort">Sort Vestments by Price:</label>
      <br />
      <select name="sort" id="sort" @change="sortVestments">
        <option value=""></option>
        <option value="asc">Lowest to Highest</option>
        <option value="desc">Highest to Lowest</option>
      </select>
    </section>
    <div class="vestments-container">
      <VestmentCard v-for="vestment in vestments" :key="vestment.id" :vestment="vestment" @click.native="selectVestment(vestment.id)" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VestmentCard from '../components/VestmentCard.vue'

export default {
  name: 'ViewVestments',
  components: {
    VestmentCard
  },
  data: () => ({
    vestments: [],
    department: ''
  }),
  mounted: async function () {
    await this.getVestments()
  },
  methods: {
    async getVestments() {
      const res = await axios.get(`http://localhost:8000/items`)
      this.vestments = res.data
    },
    sortVestments(e) {
      const sortAsc = () => {
        this.vestments.sort((a, b) => {
          return a.price - b.price
        })
      }
      const sortDesc = () => {
        this.vestments.sort((a, b) => {
          return b.price - a.price
        })
      }
      e.target.value === 'asc' ? sortAsc() : sortDesc()
    },
    selectVestment(vestmentId) {
      this.$router.push(`/details/${vestmentId}`)
    }
  }
}
</script>
