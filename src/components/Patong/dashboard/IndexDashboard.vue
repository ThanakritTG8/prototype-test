<template>
  <div id="index-dashboard">
    <h1 class="title text-center">Patong Dashboard</h1>
    <div class="row">
      <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <count-comment />
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <count-pos />
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <count-neg />
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-6 text-center">
        <div class="card">
          
            <b-overlay :show="busyLine" rounded="lg" opacity="0.6">
              <date />
            </b-overlay>
         
        </div>
      </div>
      <div class="col-lg-6">
        <div class="card">
          
            <b-overlay :show="busyWord" rounded="lg" opacity="0.6">
              <alltext-sense />
            </b-overlay>
         
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Date from "@/components/Patong/dashboard/Date";
import CountComment from "@/components/Patong/dashboard/CountComment";
import CountPos from "@/components/Patong/dashboard/CountPos";
import CountNeg from "@/components/Patong/dashboard/CountNeg";
import AlltextSense from "@/components/Patong/dashboard/AlltextSense";

export default {
  name: "index-dashboard",
  components: {
    Date,
    CountComment,
    CountPos,
    CountNeg,
    AlltextSense,
  },
  data() {
    return {
      busyWord: true,
       busyLine: true,
      timeout: null,
    };
  },

  mounted() {
    setTimeout(() => {
      this.busyWord = false;
    }, 2000);
    setTimeout(() => {
      this.busyLine = false;
    }, 500);
  },
};
</script>

<style scoped>
.card {
  margin: 20px;
  border-radius: 30px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.title {
  margin: 20px;
}
</style>