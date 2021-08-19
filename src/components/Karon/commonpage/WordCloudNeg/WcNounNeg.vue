<template>
  <div>
    <h4 class="text-center">Noun</h4>
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
  name: "common-word-cloud-noun",
  components: {
    wordcloud,
  },

  data: () => ({
    defaultWords: [],
  }),

  mounted() {
    var arr = [];
    this.$axios
      .get("https://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/karon/wordcloud/negNOUN.json")
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
