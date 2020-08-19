<template>
  <div>
    
    <b-container class="margin-top">
      <b-row>
        <b-col lg="4"></b-col>

        <b-col>
          <PieNeg />
        </b-col>

        <b-col></b-col>
      </b-row>
    </b-container>

   <b-container class="margin-top">
      <b-row>
        <b-col>
          <b-button variant="info" @click="Bar">Bar</b-button>
          <b-button variant="info" @click="Wc">WordCloud</b-button>
        </b-col>
        <b-col></b-col>
        <b-col></b-col>
      </b-row>
    </b-container>

    <b-container class="margin-top">
      <b-row>
        <b-col class="margin-top">
          <b-card class="card">
            <BarNounPos v-if="bar"/>
            <WcNoun v-if="wc"/>
          </b-card>
        </b-col>

        <b-col class="margin-top">
          <b-card class="card">
            <BarVerbPos v-if="bar"/>
            <WcVerb v-if="wc"/>
          </b-card>
        </b-col>

        <div class="w-100"></div>

        <b-col class="margin-top">
          <b-card class="card">
            <BarAdjPos v-if="bar" />
             <WcAdj v-if="wc"/>
          </b-card>
        </b-col>

        <b-col class="margin-top">
          <b-card class="card">
            <BarAdvPos v-if="bar"/>
            <WcAdv v-if="wc"/>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import PieNeg from "@/components/commonpage/PieNeg";
import BarNounPos from "@/components/commonpage/BarNounPos";
import BarVerbPos from "@/components/commonpage/BarVerbPos";
import BarAdjPos from "@/components/commonpage/BarAdjPos";
import BarAdvPos from "@/components/commonpage/BarAdvPos";

import WcNoun from "@/components/commonpage/WcNoun";
import WcVerb from "@/components/commonpage/WcVerb";
import WcAdv from "@/components/commonpage/WcAdv";
import WcAdj from "@/components/commonpage/WcAdj";
export default {
    data:()=>({
        bar : true,
        wc : false

    }) ,
    methods:{
        Wc(){
            this.bar = false;
            this.wc = true
            
        },
           Bar(){
            this.bar = true;
            this.wc = false
            
        }
    }
    ,
  components: {
    PieNeg,

    BarNounPos,
    BarVerbPos,
    BarAdjPos,
    BarAdvPos,
    WcNoun,
    WcVerb,
    WcAdv,
    WcAdj
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