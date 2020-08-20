<template>
  <div id="comment-page">
    <h1>Comment Page</h1>
    <div class="row" id="body-comment-page">
      <div class="col-1"></div>
      <div class="col-lg-10">
        <all-comment id="all-comment" />
      </div>
      <div class="col-1"></div>
      <!-- <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <pos-neg id="pos-neg" />
          </div>
        </div>
      </div>-->
    </div>
  </div>
</template>

<script>
import AllComment from "@/components/commentpage/AllComment";

export default {
  name: "comment-page",
  components: {
    AllComment,
  },
};
</script>

<style scoped>
.card {
  border-radius: 20px;
}
#body-comment-page {
  margin-top: 20px;
}
h1 {
  margin: 40px;
}
</style>