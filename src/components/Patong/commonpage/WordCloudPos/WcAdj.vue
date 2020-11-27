<template>
  <div>
    <h4 class="text-center">Adjective</h4>
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
  </div>
</template>

<script>
import wordcloud from "vue-wordcloud";
export default {
  name: "common-word-cloud-adj",
  components: {
    wordcloud,
  },
  data: () => ({
    defaultWords: [],
  }),
  //  methods: {
  //     wordClickHandler(name) {
  //       this.name = name;
  //     },
  //   },
  mounted() {
    var arr = [];
    this.$axios
      .get("http://ajkitsiri.ddns.net/wordcloud/posADJ")
      .then(({ data }) => {
        for (const key in data) {
          for (let s = 0; s < 1; s++) {
            if (data[key].count > 5) {
              arr.push(data[key]);
            }
          }
        }
        this.defaultWords = arr;
      });
  },
};
</script>
<style  scoped>
.wordcloud {
  height: 250px;
}
</style>