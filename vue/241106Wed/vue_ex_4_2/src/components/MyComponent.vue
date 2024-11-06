<template>
  <div>
    <header class="bg-success text-center py-3 fixed-top">
      <h1>My Gallery</h1>
    </header>

    <main class="container mt-5 pt-5">
      <div class="row">
        <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" v-for="item in numberOfItems" :key="item">
          <div class="card" style="width: 18rem;">
            <img src="@/assets/sample.png" class="card-img-top" alt="Sample Image">
            <div class="card-body">
              <h5 class="card-title">Card {{ item }}</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
const numberOfItems = 4
</script>

<style scoped>

</style>