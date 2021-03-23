<template>
  <div id="tab-noun">
    <b-card no-body>
      <b-tabs pills card vertical class="b-tab scroll">
        <word-card-noun-neg
          id="tab"
          :itemData="item"
          :arrData="arr"
          :per-page="perPage"
          :current-page="currentPage"
        />
      </b-tabs>
    </b-card>
    <!-- <b-pagination
      id="paginate"
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      first-text="First"
      prev-text="Prev"
      next-text="Next"
      last-text="Last"
      aria-controls="tab"
    ></b-pagination> -->
  </div>
</template>

<script>
import WordCardNounNeg from '@/components/Patong/negrelatedword/WordCardNounNeg'
export default {
  name: "tab-noun",
  components: {
    WordCardNounNeg
  },
  data: () => ({
    item: undefined,
    arr: [],
    currentPage: 1,
    perPage: 10
  }),
  mounted() {
    this.$axios
      .get("http://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/patong/postgards/NEGNOUN.json")
      .then(({ data }) => {
        for (let key in data) {
          this.item = data;
          this.arr.push(data[key].word);
        }
        // console.log(this.arr);
        //   this.arr.forEach(element => console.log(element));
      });
  },
  computed: {
    rows() {
      return this.arr.length;
    }
  },
  methods: {
    paginate(currentPage) {
      dispatch("paginate", { currentPage, perPage: this.perPage });
    }
  }
};
</script>

<style scoped>
.b-tab{
  height: 500px;
  overflow-y: scroll;
}
#paginate {
  margin-top: 20px;
}
</style>
