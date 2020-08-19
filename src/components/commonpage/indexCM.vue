<template>
  <div id="index" class="margin-top">
    <b-container class="margin-top">
      <b-row>
        <b-col>
          <b-button variant="info">Positive</b-button>
          <b-button variant="info">Negative</b-button>
        </b-col>
        <b-col></b-col>
        <b-col></b-col>
      </b-row>
    </b-container>

    <b-container class="margin-top">
      <b-row>
        <b-col lg="4"></b-col>
        <b-col>
          <PiePos />
        </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
    <b-container class="margin-top">
      <b-row>
        <b-col class="margin-top">
          <BarNounPos />
        </b-col>
        <b-col class="margin-top">
          <BarVerbPos />
        </b-col>
        <div class="w-100"></div>
        <b-col class="margin-top">
          <BarAdjPos />
        </b-col>
        <b-col class="margin-top">
          <BarAdvPos />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import PiePos from "@/components/commonpage/PiePos";
import BarNounPos from "@/components/commonpage/BarNounPos";
import BarVerbPos from "@/components/commonpage/BarVerbPos";
import BarAdjPos from "@/components/commonpage/BarAdjPos";
import BarAdvPos from "@/components/commonpage/BarAdvPos";
export default {
  components: {
    PiePos,
    BarNounPos,
    BarVerbPos,
    BarAdjPos,
    BarAdvPos,
  },
};
</script>
<style  scoped>

.margin-top{
    margin-top: 20px;
}
</style>