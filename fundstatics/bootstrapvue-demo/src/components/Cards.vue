<template>
  <div>

    <b-carousel
      id="carousel-1"
      :interval="2000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      style="text-shadow: 1px 1px 2px #333;"

    >
      <!-- Text slides with image -->
      <b-carousel-slide

        img-src="http://81.70.21.205/img/data_analysize.jpg"
      ></b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide

              img-src="http://81.70.21.205/img/python.jpeg"  >

      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide

              img-src="http://81.70.21.205/img/laravel.png"  ></b-carousel-slide>

      <!-- Slides with img slot -->

    </b-carousel>




<br>
<br>
<br>
<br>

    <div class="text-center">
  <h2>专栏介绍 <b-badge>New</b-badge></h2>

  <h6>Example heading <b-badge>New</b-badge></h6>
</div>
   <b-container>
    <div v-if="meals.length">
      <b-row>
        <div v-bind:key="data.index" v-for="data in meals">
          <b-col l="3">
            <b-card
              v-bind:title="data.strCategory"
              v-bind:img-src="data.strCategoryThumb"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2">
              <b-card-text>{{ `${data.strCategoryDescription.slice(0,100)}...` }}</b-card-text>
              <b-button href="#" variant="primary">View food</b-button>
            </b-card>
          </b-col>
        </div>
      </b-row>
    </div>
    <div v-else>
      <h5>No meals available yet ?</h5>
    </div>
  </b-container>


  </div>





</template>
<style>
 .w-100 {
    height: 400px !important;;
  }
</style>
<script>
  import axios from "axios";

  export default {

    data() {
     return {
      meals: []
    };
    },
    mounted() {
    axios
      .get("https://www.themealdb.com/api/json/v1/1/categories.php")
      .then(response => {

        this.meals = response.data.categories.slice(0,3);
      })
      .catch(err => {
        console.log(err);
      });
  }
  }
</script>