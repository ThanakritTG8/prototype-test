<template>
  <div id="neg-type-card">
    <b-tabs
      fill
      class="b-card shadow p-3 mb-5 bg-white rounded"
      align="center"
      active-nav-item-class="font-weight-bold text-uppercase text-success"
    >
      <b-tab title="Noun" class="tab" active>
        <tab-noun-neg />
      </b-tab>
      <b-tab title="Verb" class="tab">
        <tab-verb-neg />
      </b-tab>
      <b-tab title="Adjective" class="tab"> 
        <tab-adj-neg />
      </b-tab>
      <b-tab title="Adverb" class="tab"> 
        <tab-adv-neg />
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import TabNounNeg from '@/components/negrelatedword/TabNounNeg'
import TabVerbNeg from '@/components/negrelatedword/TabVerbNeg'
import TabAdjNeg from '@/components/negrelatedword/TabAdjNeg'
import TabAdvNeg from '@/components/negrelatedword/TabAdvNeg'

export default {
  name: "neg-type-card",
  components: {
    TabNounNeg,
    TabVerbNeg,
    TabAdjNeg,
    TabAdvNeg
  },
  data: () => ({}),
  mounted() {},
  methods: {}
};
</script>

<style scoped>
.b-card {
  height: 600px;
  /* height: auto; */
  margin: 10px;
}
</style>
