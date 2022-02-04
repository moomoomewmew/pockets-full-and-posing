<template>
  <div class="view-departments">
    <h1>{{ department }}</h1>
    <section class="dropdown-menu">
      <label for="sort">Sort Vestments by Price:</label>
      <br />
      <select name="sort" id="sort" @change="sortVestments">
        <option value=""></option>
        <option value="asc">Ascending</option>
        <option value="desc">Descending</option>
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
  mounted() {
    this.getVestmentsByDepartment()
    this.getDepartment()
  },
  methods: {
    async getVestmentsByDepartment() {
      const departmentId = parseInt(this.$route.params.department_id)
      const res = await axios.get(`http://localhost:8000/departments/${departmentId}`)
      this.vestments = res.data.items
    },
    getDepartment () {
      this.department = this.$route.params.department_name
    },
    sortVestments(e) {
      const sortAsc = () => {
        this.vestments.sort((a, b) => {
          return a.rating - b.rating
        })
      }
      const sortDesc = () => {
        this.vestments.sort((a, b) => {
          return b.rating - a.rating
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
