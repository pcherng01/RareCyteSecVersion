<template>
  <div id="app">
    <mdb-container class="mt-5">
    <mdb-row>
      <GalleryComponent
        v-for="imageName in imageNameList"
        :key="imageName.id"
        :imageName="imageName"
        />
    </mdb-row>
  </mdb-container>
  </div>
</template>

<script>
import GalleryComponent from './components/GalleryComponent.vue'
import {mdbContainer, mdbRow} from "mdbvue";
const axios = require('axios').default;

export default {
  name: 'App',
  components: {
    GalleryComponent,
    mdbContainer,
    mdbRow
  },
  data: function() {
    return {
      imageNameList: [],
    }
  },
  methods: {
    getImageList() {
      const path = 'http://localhost:5000/images/list';
      axios.get(path)
        .then((res) => {
          this.imageNameList = res.data
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getImageList();
  },
}
</script>

<style lang="scss">
$image-path: '~@/../mdb/mdbvue/img';
@import '~@/../mdb/mdbvue/scss/mdb-free.scss';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
