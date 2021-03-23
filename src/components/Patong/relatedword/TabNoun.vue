<template>
  <div id="tab-noun">
    <b-card no-body>
      <b-tabs pills card vertical class="b-tab">
        <word-card-noun
          id="tab"
          :itemData="item"
          :arrData="arr"
          :per-page="perPage"
          :current-page="currentPage"
          :filter="filter"
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
import WordCardNoun from "@/components/Patong/relatedword/WordCardNoun";
export default {
  name: "tab-noun",
  components: {
    WordCardNoun
  },
  data: () => ({
    busy: true,
    item: undefined,
    arr: [],
    currentPage: 1,
    perPage: 10,
    filter: null
  }),
  mounted() {
    this.$axios
      .get("http://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/patong/postgards/POSNOUN.json")      
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
    },
    sortOptions() {
      // Create an options list from our fields
      return this.item.filter().map(i => {
        return { text: i.word, value: i.sentence };
      });
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
.b-tab {
  height: 500px;
  overflow-y: scroll;
}
#paginate {
  margin-top: 20px;
}
.text-right {
  margin-top: 60px;

  margin-right: -140px;
  font-size: 120px;
}
.overley {
  margin-top: 100px;
  font-size: 160px;
}

</style>
