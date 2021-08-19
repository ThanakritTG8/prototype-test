<template>
  <div>
    <h4 class="text-center">Verb</h4>
    <wordcloud
      v-b-modal.modal-scrollableVerb
      class="wordcloud"
      :data="defaultWords"
      nameKey="word"
      valueKey="count"
      :color="Accent"
      :showTooltip="true"
      :wordClick="wordClickHandlerVerb"
    ></wordcloud>
  </div>
</template>

<script>
import wordcloud from "vue-wordcloud";
export default {
  name: "common-word-cloud-vreb",
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
      .get("https://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/karon/wordcloud/posVERB.json")
      .then(({ data }) => {
        for (const key in data) {
          for (let s = 0; s < 1; s++) {
            if (data[key].count > 10) {
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
.position {
  margin: 30px;
}
.boder {
  border-radius: 30px;
  margin: 15px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 3px 10px 0 rgba(0, 0, 0, 0.19);
}
</style>