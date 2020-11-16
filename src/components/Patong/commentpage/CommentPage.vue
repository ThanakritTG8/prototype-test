<template>
  <div id="comment-page">
    <NavBar />
    <b-tabs content-class="mt-3" class="margin">
      <b-tab title="All Comment" active>
        <div class="padding">
          <all-comment id="all-comment" />
        </div>
      </b-tab>
      <b-tab title="Positive"><p>Positive</p></b-tab>
      <b-tab title="Negative"><p>Negative</p></b-tab>
    </b-tabs>
  </div>
</template>

<script>
import AllComment from "@/components/Patong/commentpage/AllComment";
import NavBar from "@/layout/NavBar";
export default {
  name: "comment-page",
  components: {
    AllComment,
    NavBar,
  },
};
</script>

<style scoped>
.card {
  border-radius: 20px;
}
#body-comment-page {
  margin-top: 100px;
}
h1 {
  margin: 40px;
}
.padding {
  padding: 40px;
}
.margin {
  margin: 30px;
}
</style>