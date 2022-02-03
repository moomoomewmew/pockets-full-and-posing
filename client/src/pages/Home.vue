<template>
  <div>Home</div>
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
    searched: false
  }),
mounted:async ()=> {
  await this.getDepartments()
},
methods: {
  async getDepartments() {
    const res = await axios.get(`http://localhost:8000/departments`)
    this.departments = res
  }
}

}
</script>