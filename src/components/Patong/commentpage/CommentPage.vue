<template>
  <div id="comment-page">
    <NavBar />
  
    <b-tabs content-class="mt-3" class="margin">
      <b-tab title="All Comments" active>
        <div class="padding">
           
          <AllComment />
      
        </div>
      </b-tab>
    
      <b-tab title="Positive">
        <div class="padding">
          <PositiveComment />
        </div>
      </b-tab>
      <b-tab title="Negative">
        <div class="padding">
          <NegativeComment />
        </div>
      </b-tab>
    </b-tabs>
    
  </div>
</template>

<script>
import NegativeComment from "@/components/Patong/commentpage/NegativeComment";
import PositiveComment from "@/components/Patong/commentpage/PositiveComment";
import AllComment from "@/components/Patong/commentpage/AllComment";
import NavBar from "@/layout/NavBar";
export default {
  name: "comment-page",
  components: {
    AllComment,
    NavBar,
    PositiveComment,
    NegativeComment,
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