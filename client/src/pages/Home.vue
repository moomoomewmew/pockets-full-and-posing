<template>
  <div>
    <div class = "search">
      <form @submit="getSearchResults" v-on:keyup.enter="getSearchResults" >
        <input
        type="text"
        :value="searchQuery"
        @input="handleChange"
         />
        <button type="submit">Fetch</button>
      </form>
      
      <h2 v-if="searched">Search Results</h2>
      <section class="search-results">

        <VestmentCard v-for="vestment in searchResults" :key="vestment.id" :vestment="vestment" @click.native="selectVestment(vestment.id)"/>

      </section>
    </div>
    <div class="departments" v-if="!searched">
      <h2>Departments</h2>
      <section class="department-card-container">
      
        <DepartmentCard v-for="department in departments" :key="department.id" :department="department" @click.native="selectDepartment(department.id, department.name)"/>

      </section>

    </div>
  </div>
</template>
 
 
 
<script> 
import axios from 'axios'
// import components
import DepartmentCard from '../components/DepartmentCard.vue'
import VestmentCard from '../components/VestmentCard.vue'

export default {
  name: 'Home',
  components: {
    DepartmentCard,
    VestmentCard
  },
  data: () => ({
    departments: [],
    searchQuery: '',
    searchResults: [],
    searched: false,
    vestments: []
  }),
mounted: async function() {
 await this.getDepartments(),
 await this.getVestments()
},
methods: {
  async getDepartments() {
    const res = await axios.get(`http://localhost:8000/departments/`)
    this.departments = res.data
  },
async getVestments() {
    const res = await axios.get(`http://localhost:8000/items/`)
    this.vestments = res.data
  },
  getSearchResults(e) {
    e.preventDefault()
    const res = this.vestments.filter(vestment => vestment.name === this.searchQuery)
    this.searchResults = res
    this.searched = true
    this.searchQuery = ''
  },
  handleChange(e) {
    this.searchQuery = e.target.value

  },
  selectDepartment(departmentId, departmentName) {
    this.$router.push(`/vestments-by-department/${departmentId}/${departmentName}`)
  },
  selectVestment(vestmentId) {
    this.$router.push(`/details/${vestmentId}`)
  }
}

}
</script>