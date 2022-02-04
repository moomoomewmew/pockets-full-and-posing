<template>
  <div class="department-card">
    <div class="image-wrapper">
      <img :src="department.image" :alt="department.name" />
    </div>
    <div class="info-wrapper">
      <h3>{{ department.name }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DepartmentCard',
  props: ['department']
}
</script>
