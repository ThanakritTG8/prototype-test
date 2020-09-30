<template>
  <div id="index-dashboard-karon">
    <h1 class="title text-center">Karon Dashboard</h1>
    <div class="row">
      <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <count-comment-karon />
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <count-pos-karon />
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <count-neg-karon />
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-6 text-center">
        <div class="card">
          <div class="card-body">
            <date-karon />
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
import CountCommentKaron from '@/components/dashboardKaron/CountCommentKaron'
import CountNegKaron from '@/components/dashboardKaron/CountNegKaron'
import CountPosKaron from '@/components/dashboardKaron/CountPosKaron'
import DateKaron from '@/components/dashboardKaron/DateKaron'
import AlltextSense from '@/components/Patong/dashboard/AlltextSense'

export default {
  name: "index-dashboard-karon",
  components: {
    DateKaron,
    CountCommentKaron,
    CountPosKaron,
    CountNegKaron,
    AlltextSense,
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