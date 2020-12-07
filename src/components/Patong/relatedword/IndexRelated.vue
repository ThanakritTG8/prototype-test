<template>
  <div id="index-related">
    <NavBar />
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
import NavBar from "@/layout/NavBar";
import PosTypeCard from "@/components/Patong/relatedword/PosTypeCard";
import NegTypeCard from "@/components/Patong/negrelatedword/NegTypeCard";
export default {
  name: "index-related",
  components: {
    PosTypeCard,
    NegTypeCard,
    NavBar,
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
