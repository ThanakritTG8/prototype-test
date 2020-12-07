<template>
  <div>
    <b-container class="margin-top">
      <b-row>
        <b-col cols="2" lg="4"></b-col>

        <b-col cols="8" lg="4">
          <PieNeg />
        </b-col>
        <b-col cols="2"></b-col>
      </b-row>
    </b-container>

    <b-container class="margin-top">
      <b-row>
        <b-col cols="2" style="text-align: right">
          <b-button variant="info" @click="Bar">Bar Chart</b-button>
        </b-col>
        <b-col cols="3" style="text-align: left">
          <b-button variant="info" @click="Wc">WordCloud</b-button>
        </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>

    <b-container class="margin-top">
      <b-row>
        <b-col class="margin-top" col-lg-6>
          <b-card class="card">
            <b-overlay :show="busy" rounded="lg" opacity="0.6">
              <BarNounNeg v-if="bar" />
              <WcNounNeg v-if="wc" />
            </b-overlay>
          </b-card>
        </b-col>

        <b-col class="margin-top" col-lg-6>
          <b-card class="card">
            <b-overlay :show="busy" rounded="lg" opacity="0.6">
              <BarVerbNeg v-if="bar" />
              <WcVerbNeg v-if="wc" />
            </b-overlay>
          </b-card>
        </b-col>

        <div class="w-100"></div>

        <b-col class="margin-top" col-lg-6>
          <b-card class="card">
            <b-overlay :show="busy" rounded="lg" opacity="0.6">
              <BarAdjNeg v-if="bar" />
              <WcAdjNeg v-if="wc" />
            </b-overlay>
          </b-card>
        </b-col>

        <b-col class="margin-top" col-lg-6>
          <b-card class="card">
            <b-overlay :show="busy" rounded="lg" opacity="0.6">
              <BarAdvNeg v-if="bar" />
              <WcAdvNeg v-if="wc" />
            </b-overlay>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import PieNeg from "@/components/Karon/commonpage/PieNeg";
import BarNounNeg from "@/components/Karon/commonpage/BarNeg/BarNounNeg";
import BarVerbNeg from "@/components/Karon/commonpage/BarNeg/BarVerbNeg";
import BarAdjNeg from "@/components/Karon/commonpage/BarNeg/BarAdjNeg";
import BarAdvNeg from "@/components/Karon/commonpage/BarNeg/BarAdvNeg";

import WcNounNeg from "@/components/Karon/commonpage/WordCloudNeg/WcNounNeg";
import WcVerbNeg from "@/components/Karon/commonpage/WordCloudNeg/WcVerbNeg";
import WcAdvNeg from "@/components/Karon/commonpage/WordCloudNeg/WcAdvNeg";
import WcAdjNeg from "@/components/Karon/commonpage/WordCloudNeg/WcAdjNeg";
export default {
  data: () => ({
    bar: true,
    wc: false,
    busy: false,
    timeout: null
  }),
  methods: {
    Wc() {
      this.bar = false;
      this.wc = true;
      this.busy = true;
      setTimeout(() => {
        this.busy = false;
      }, 2200);
    },
    Bar() {
      this.bar = true;
      this.wc = false;
    }
  },
  components: {
    PieNeg,

    BarNounNeg,
    BarVerbNeg,
    BarAdjNeg,
    BarAdvNeg,

    WcNounNeg,
    WcVerbNeg,
    WcAdvNeg,
    WcAdjNeg
  }
};
</script>
<style scoped>
.margin-top {
  margin-top: 20px;
}
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  border-radius: 20px;
}
</style>
