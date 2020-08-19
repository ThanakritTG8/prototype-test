<template>
  <div id="index-dashboard">
    <h1 class="title text-center">Dashboard</h1>
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
          <div class="card-body">
            <date />
          </div>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <alltext-sense />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Date from "@/components/dashboard/Date";
import CountComment from "@/components/dashboard/CountComment";
import CountPos from "@/components/dashboard/CountPos";
import CountNeg from "@/components/dashboard/CountNeg";
import AlltextSense from "@/components/dashboard/AlltextSense";

export default {
  name: "index-dashboard",
  components: {
    Date,
    CountComment,
    CountPos,
    CountNeg,
    AlltextSense,
  },
};
</script>

<style scoped>
.card {
  margin: 20px;
  border-radius: 30px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  border-radius: 20px;
}
.title {
  margin: 20px;
}
</style>