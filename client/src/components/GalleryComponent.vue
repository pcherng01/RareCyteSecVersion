<template>
      <mdb-col lg="4" md="12" class="mb-4">
        <a @click="showModal = true">
          <img class="img-fluid z-depth-1" :src="getImage()"
          alt="video" data-toggle="modal" data-target="#modal1">
        </a>
        <mdb-modal size="lg" :show="showModal" @close="showModal = false">
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">{{this.metadata}}</span>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
</template>

<script>
  const axios = require('axios').default;
  import {mdbCol, mdbBtn, mdbModal, mdbModalFooter} from "mdbvue";
  export default {
    name: "GalleryPage",
    data: function () {
      return {
          showModal: false,
          metadata: ''
      }
    },
    props: ['imageName'],
    components: {
      mdbCol,
      mdbBtn,
      mdbModal,
      mdbModalFooter,
    },
    methods: {
      getImage() {
        const path = 'http://localhost:5000/images/' + this.imageName;
        return path;
      },
      getMetaData() {
        const path = 'http://localhost:5000/images/metadata/' + this.imageName;
        axios.get(path)
        .then((res) => {
          this.metadata = res.data;
        })
        .catch((error) => {
          console.error(error);
        })
      }
    },
    created() {
      this.getImage();
      this.getMetaData();
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @media (min-width: 768px) {
    .carousel-multi-item-2 .col-md-3 {
      float: left;
      width: 25%;
      max-width: 100%; } }

    .carousel-multi-item-2 .card img {
      border-radius: 2px; }

    figure {
      cursor: pointer;
    }
</style>
