<template>
  <div id="pos-type-card">
    <b-overlay :show="busyLine" rounded="lg" opacity="0.6">
      <b-tabs
        fill
        class="b-card shadow p-3 mb-5 bg-white rounded"
        align="center"
        active-nav-item-class="font-weight-bold text-uppercase text-success"
      >
        <b-tab title="Place" class="tab" active>
          <tab-noun />
        </b-tab>
        <b-tab title="Action" class="tab">
          <tab-verb />
        </b-tab>
        <b-tab title="Emotion" class="tab">
          <tab-adj />
        </b-tab>
        <b-tab title="Character" class="tab">
          <tab-adv />
        </b-tab>
      </b-tabs>
    </b-overlay>
  </div>
</template>

<script>
import TabNoun from "@/components/relatedword/TabNoun";
import TabVerb from "@/components/relatedword/TabVerb";
import TabAdj from "@/components/relatedword/TabAdj";
import TabAdv from "@/components/relatedword/TabAdv";
export default {
  name: "pos-type-card",
  components: {
    TabNoun,
    TabVerb,
    TabAdj,
    TabAdv,
  },
  data: () => ({
    busyLine: true,
  }),
  mounted() {
    setTimeout(() => {
      this.busyLine = false;
    }, 10000);
  },
  methods: {},
};
</script>

<style scoped>
.b-card {
  height: 600px;
  /* height: auto; */
  margin: 10px;
}
</style>
