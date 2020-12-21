<template>
  <div>
    <h4 class="text-center">Adverb</h4>
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
    
    this.$axios
      .get("http://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/karon/wordcloud/negADV.json")
      .then(({ data }) => {
        
        this.defaultWords = data;
      });
  },
};
</script>
<style  scoped>
.wordcloud {
  height: 250px;
}
</style>