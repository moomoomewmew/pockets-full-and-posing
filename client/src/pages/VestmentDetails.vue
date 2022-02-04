<template>
  <div class="vestment-content" >
    <section class="image-container">
      <div>
        <img :src="vestment.image" />
        
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
      </div>
    </section>
  </div>
</template>

<script>

  
export default {
  
  name: 'VestmentDetails',
  props: ['vestment']
  
 
  }

</script>