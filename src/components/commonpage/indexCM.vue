<template>
  <div id="index" class="margin-top">
    <b-container class="margin-top">
      <b-row>
        <b-col>
          <b-button variant="info" @click="PosBtn">Positive</b-button>
          <b-button variant="info" @click="NegBtn">Negative</b-button>
        </b-col>
        <b-col></b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
  <PosPage v-if="pos"/>
  <NegPage v-if="neg"/>
  </div>
</template>
<script>
import NegPage from "@/components/commonpage/NegPage";
import PosPage from "@/components/commonpage/PosPage";
export default {
  data :()=>({
    pos : true ,
    neg :false
  }),
  methods :{
    PosBtn(){
      this.pos = true
      this.neg =false
    },
     NegBtn(){
      this.pos = false
      this.neg =true
    }
  }
  ,components : {
PosPage,
NegPage
  }
   
};
</script>
<style  scoped>

.margin-top{
    margin-top: 20px;
    
}
.card{
  background-color: white;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  border-radius: 20px;
}
</style>