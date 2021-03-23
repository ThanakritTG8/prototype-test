<template>
  <div id="all-text-sense">
  
    
    <wordcloud
      v-b-modal.modal-scrollable
      class="wordcloud"
      :data="defaultWords"
      nameKey="word"
      valueKey="count"
      :color="Accent"
      :showTooltip="true"
      :wordClick="wordClickHandler"
    ></wordcloud>

    <b-modal id="modal-scrollable" ok-only size="lg" scrollable>
      <template v-slot:modal-title>
        <h3>
          #
          <code>{{ name }}</code>
        </h3>
      </template>

      <div class="card">
        <div class="card-body">
          <!-- Main table element -->
          <b-table
            show-empty
            small
            stacked="md"
            :items="item"
            :fields="fields"
            :filter="filter"
             
          >
         
           <template #cell(Thai)="data">
              <text-highlight :queries="filter">{{
                data.item.Thai
              }}</text-highlight>
            </template>
          </b-table>
        </div>
      </div>
    </b-modal>
  </div>
</template>

<script>
import wordcloud from "vue-wordcloud";

export default {
  name: "all-text-sense",
  components: {
    wordcloud,
  },
  methods: {
    wordClickHandler(name) {
      this.name = name;
      this.filter = name;
    },
  },

  data: () => ({
    name: "null",
    defaultWords: [],
    item: [],

    fields: [
      {
        key: "Thai",
        label: "Review",
      },
    ],
    filter: [],
  }),
  mounted() {
    var arr = [];
    this.$axios.get("http://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/patong/wordcloud/all.json").then(({ data }) => {
      for (const key in data) {
        for (let s = 0; s < 1; s++) {
          if (data[key].count > 20) {
            arr.push(data[key]);
          }
        }
      }
      this.defaultWords = arr;
    });
    this.$axios.get("http://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/patong/allcomments.json").then(({ data }) => {
      this.item = data;
    });
  },
};
</script>

<style scoped>

.right {
  text-align: right;
}
</style>