<template>
  <mdb-container class="mt-5">
    <mdb-row>
      <!-- Grid column -->
      <mdb-col lg="4" md="12" class="mb-4">
        <a @click="showModal = true"><img class="img-fluid z-depth-1" src="https://mdbootstrap.com/img/screens/yt/screen-video-1.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal" @close="showModal = false">
          <mdb-modal-body class="mb-0 p-0">
            <div class="embed-responsive embed-responsive-16by9 z-depth-1-half">
              <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/A3PDXmYoF5U"
                allowfullscreen></iframe>
            </div>
          </mdb-modal-body>
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <a class="btn-floating btn-sm btn-fb"><i class="fab fa-facebook"></i></a>
            <!--Twitter-->
            <a class="btn-floating btn-sm btn-tw"><i class="fab fa-twitter"></i></a>
            <!--Google +-->
            <a class="btn-floating btn-sm btn-gplus"><i class="fab fa-google-plus"></i></a>
            <!--Linkedin-->
            <a class="btn-floating btn-sm btn-ins"><i class="fab fa-linkedin-in"></i></a>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
      <!-- Grid column -->
      <mdb-col lg="4" md="6" class="mb-4">
        <a @click="showModal2 = true"><img class="img-fluid z-depth-1" src="https://mdbootstrap.com/img/screens/yt/screen-video-2.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal2" @close="showModal2 = false">
          <mdb-modal-body class="mb-0 p-0">
            <div class="embed-responsive embed-responsive-16by9 z-depth-1-half">
              <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/wTcNtgA6gHs"
                allowfullscreen></iframe>
            </div>
          </mdb-modal-body>
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <a class="btn-floating btn-sm btn-fb"><i class="fab fa-facebook"></i></a>
            <!--Twitter-->
            <a class="btn-floating btn-sm btn-tw"><i class="fab fa-twitter"></i></a>
            <!--Google +-->
            <a class="btn-floating btn-sm btn-gplus"><i class="fab fa-google-plus"></i></a>
            <!--Linkedin-->
            <a class="btn-floating btn-sm btn-ins"><i class="fab fa-linkedin-in"></i></a>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal2 = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
      <!-- Grid column -->
      <mdb-col lg="4" md="6" class="mb-4">
        <a @click="showModal3 = true"><img class="img-fluid z-depth-1" src="https://mdbootstrap.com/img/screens/yt/screen-video-3.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal3" @close="showModal3 = false">
          <mdb-modal-body class="mb-0 p-0">
            <div class="embed-responsive embed-responsive-16by9 z-depth-1-half">
              <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/vlDzYIIOYmM"
                allowfullscreen></iframe>
            </div>
          </mdb-modal-body>
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <a class="btn-floating btn-sm btn-fb"><i class="fab fa-facebook"></i></a>
            <!--Twitter-->
            <a class="btn-floating btn-sm btn-tw"><i class="fab fa-twitter"></i></a>
            <!--Google +-->
            <a class="btn-floating btn-sm btn-gplus"><i class="fab fa-google-plus"></i></a>
            <!--Linkedin-->
            <a class="btn-floating btn-sm btn-ins"><i class="fab fa-linkedin-in"></i></a>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal3 = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
      <!-- Grid column -->
      <mdb-col lg="4" md="6" class="mb-4">
        <a @click="showModal4 = true"><img class="img-fluid z-depth-1" src="https://mdbootstrap.com/img/screens/yt/screen-video-4.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal4" @close="showModal4 = false">
          <mdb-modal-body class="mb-0 p-0">
            <div class="embed-responsive embed-responsive-16by9 z-depth-1-half">
              <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/vlDzYIIOYmM"
                allowfullscreen></iframe>
            </div>
          </mdb-modal-body>
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <a class="btn-floating btn-sm btn-fb"><i class="fab fa-facebook"></i></a>
            <!--Twitter-->
            <a class="btn-floating btn-sm btn-tw"><i class="fab fa-twitter"></i></a>
            <!--Google +-->
            <a class="btn-floating btn-sm btn-gplus"><i class="fab fa-google-plus"></i></a>
            <!--Linkedin-->
            <a class="btn-floating btn-sm btn-ins"><i class="fab fa-linkedin-in"></i></a>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal4 = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
      <!-- Grid column -->
      <mdb-col lg="4" md="6" class="mb-4">
        <a @click="showModal4 = true"><img class="img-fluid z-depth-1" src="https://mdbootstrap.com/img/screens/yt/screen-video-5.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal4" @close="showModal4 = false">
          <mdb-modal-body class="mb-0 p-0">
            <div class="embed-responsive embed-responsive-16by9 z-depth-1-half">
              <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/vlDzYIIOYmM"
                allowfullscreen></iframe>
            </div>
          </mdb-modal-body>
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <a class="btn-floating btn-sm btn-fb"><i class="fab fa-facebook"></i></a>
            <!--Twitter-->
            <a class="btn-floating btn-sm btn-tw"><i class="fab fa-twitter"></i></a>
            <!--Google +-->
            <a class="btn-floating btn-sm btn-gplus"><i class="fab fa-google-plus"></i></a>
            <!--Linkedin-->
            <a class="btn-floating btn-sm btn-ins"><i class="fab fa-linkedin-in"></i></a>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal4 = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
      <!-- Grid column -->
      <mdb-col lg="4" md="6" class="mb-4">
        <a @click="showModal6 = true"><img class="img-fluid z-depth-1" src="https://mdbootstrap.com/img/screens/yt/screen-video-6.jpg" alt="video" data-toggle="modal" data-target="#modal1"></a>
        <mdb-modal size="lg" :show="showModal6" @close="showModal6 = false">
          <mdb-modal-body class="mb-0 p-0">
            <div class="embed-responsive embed-responsive-16by9 z-depth-1-half">
              <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/vlDzYIIOYmM"
                allowfullscreen></iframe>
            </div>
          </mdb-modal-body>
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word!</span>
            <a class="btn-floating btn-sm btn-fb"><i class="fab fa-facebook"></i></a>
            <!--Twitter-->
            <a class="btn-floating btn-sm btn-tw"><i class="fab fa-twitter"></i></a>
            <!--Google +-->
            <a class="btn-floating btn-sm btn-gplus"><i class="fab fa-google-plus"></i></a>
            <!--Linkedin-->
            <a class="btn-floating btn-sm btn-ins"><i class="fab fa-linkedin-in"></i></a>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal6 = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
      </mdb-col>
      <!-- Grid column -->
    </mdb-row>
  </mdb-container>
</template>

<script>
  import {
    mdbContainer,
    mdbRow,
    mdbCol,
    // mdbIcon,
    mdbBtn,
    // mdbLightbox,
    // mdbCarousel,
    // mdbCard,
    mdbModal,
    // mdbModalHeader,
    // mdbModalTitle,
    // dbModalBody,
    mdbModalFooter,
    // mdbNavItem
  } from "mdbvue";
  export default {
    name: "GalleryPage",
    data() {
      return {
        showModal: false,
        showModal2: false,
        showModal3: false,
        showModal4: false,
        showModal5: false,
        showModal6: false
      };
    },
    components: {
      mdbContainer,
      mdbRow,
      mdbCol,
      // mdbIcon,
      mdbBtn,
      // mdbLightbox,
      // mdbCarousel,
      // mdbCard,
      mdbModal,
      // mdbModalHeader,
      // mdbModalTitle,
      // mdbModalBody,
      mdbModalFooter,
      // mdbNavItem
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
