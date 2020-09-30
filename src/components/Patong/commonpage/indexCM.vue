<template>
  <div id="index" >
    <NavBar/>
    <div class="margin-top">
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="3" style="text-align: right; margin-left:20px;">
            <b-button variant="info" @click="PosBtn">Positive</b-button>
        </b-col>
           <b-col cols="3" style="text-align: left;">
           <b-button variant="info" @click="NegBtn">Negative</b-button>
       </b-col>
          
      </b-row>
    </div>
    <PosPage v-if="pos" />
    <NegPage v-if="neg" />
  </div>
</template>
<script>
import NavBar from "@/layout/NavBar";
import NegPage from "@/components/Patong/commonpage/NegPage";
import PosPage from "@/components/Patong/commonpage/PosPage";
export default {
  data: () => ({
    pos: true,
    neg: false,
  }),
  methods: {
    PosBtn() {
      this.pos = true;
      this.neg = false;
    },
    NegBtn() {
      this.pos = false;
      this.neg = true;
    },
  },
  components: {
    PosPage,
    NegPage,
    NavBar
  },
};
</script>
<style  scoped>
.margin-top {
  margin-top: 20px;
}
.card {
  background-color: white;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  border-radius: 20px;
  
}
</style>