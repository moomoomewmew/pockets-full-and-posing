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
        <!-- vestment card here -->
      </section>
    </div>
    <div class="departments" v-if="!searched">
      <h2>Departments</h2>
      <section class="department-card-container">
        <!-- department card here  -->
      </section>

    </div>
  </div>
</template>
 
 
 
<script> 
import axios from 'axios'
// import components
export default {
  name: 'Home',
  components: {},
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
  }
}

}
</script>