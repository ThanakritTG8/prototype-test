<template>
  <div id="index-related">
    <NavKaron />
    <div id="group">
      <h1 class="title text-center">Related Word</h1>
    </div>
    <div>
      <b-card no-body class="b-card shadow-sm p-3 mb-5 bg-white rounded">
        <b-tabs
          content-class="mt-3"
          fill
          align="center"
          active-nav-item-class="font-weight-bold text-uppercase text-success"
          active-tab-class=""
        >
          <b-tab title="Positive" class="tab" active>
            <pos-type-card />
          </b-tab>
          <b-tab title="Negative" class="tab">
            <neg-type-card />
          </b-tab>
        </b-tabs>
      </b-card>
    </div>
  </div>
</template>

<script>
import NavKaron from "@/layout/NavKaron";
import PosTypeCard from "@/components/Karon/relatedword/PosTypeCard";
import NegTypeCard from "@/components/Karon/negrelatedword/NegTypeCard";
export default {
  name: "index-related",
  components: {
    PosTypeCard,
    NegTypeCard,
    NavKaron,
  },
  methods: {},
};
</script>

<style scoped>
#group {
  margin: 30px;
}
.b-card {
  /* height: 770px; */
  height: auto;
  margin-left: 20px;
  margin-right: 20px;
}
.tab {
  margin: 30px 20px 20px;
}
</style>
