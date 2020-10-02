<template>
  <div id="tab-noun">
    <b-form-group>
      <b-input-group size="sm">
        <b-form-input
          v-model="filter"
          type="search"
          id="filterInput"
          placeholder="Type to Search"
        ></b-form-input>
        <b-input-group-append>
          <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
        </b-input-group-append>
      </b-input-group>
    </b-form-group>
    <b-card no-body>
      <b-tabs pills card vertical class="b-tab scroll">
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
import WordCardNoun from "@/components/relatedword/WordCardNoun";
export default {
  name: "tab-noun",
  components: {
    WordCardNoun
  },
  data: () => ({
    item: undefined,
    arr: [],
    currentPage: 1,
    perPage: 10,
    filter: null
  }),
  mounted() {
    this.$axios
      .get("http://localhost:5000/postgards/POSNOUN")
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
      return this.item
        .filter()
        .map(i => {
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
</style>
