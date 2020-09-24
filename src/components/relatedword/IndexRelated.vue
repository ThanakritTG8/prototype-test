<template>
  <div id="index-related">
    <div id="group">
      <h1 class="title text-center">Related Word</h1>
    </div>
    <div>
      <b-tabs
        content-class="mt-3"
        fill
        align="center"
        active-nav-item-class="font-weight-bold text-uppercase text-success"
        active-tab-class=""
      >
        <b-tab title="Place" active>
          <noun-card
            id="noun"
            v-if="item"
            :itemData="item"
            :arrData="arr"
            :getRows="rows"
            :current-page="currentPage"
            :per-page="perPage"
          />
        </b-tab>
        <b-tab title="Action">
          <verb-card />
        </b-tab>
        <b-tab title="Emotion">
          <adj-card />
        </b-tab>
        <b-tab title="Character">
          <adv-card />
        </b-tab>
      </b-tabs>
      <b-pagination
        v-if="item"
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        first-text="First"
        prev-text="Prev"
        next-text="Next"
        last-text="Last"
        aria-controls="noun"
      ></b-pagination>
    </div>
  </div>
</template>

<script>
import NounCard from "@/components/relatedword/NounCard";
import VerbCard from "@/components/relatedword/VerbCard";
import AdjCard from "@/components/relatedword/AdjCard";
import AdvCard from "@/components/relatedword/AdvCard";

export default {
  name: "index-related",
  components: {
    NounCard,
    VerbCard,
    AdjCard,
    AdvCard
  },
  data: () => ({
    item: undefined,
    arr: [],
    currentPage: 1,
    perPage: 3
  }),
  mounted() {
    this.$axios
      .get("http://localhost:5000/senten/text/test/NOUN")
      .then(({ data }) => {
        this.item = data;
        for (const key in data) {
          this.arr.push(key);
        }
      });
  },
  computed: {
    rows() {
      return this.item.length;
    }
  }
};
</script>

<style scoped>
#group {
  margin: 30px;
}
</style>
