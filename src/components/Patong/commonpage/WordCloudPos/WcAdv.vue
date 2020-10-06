<template>
  <div>
    <h4 class="text-center">Charecter</h4>
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
  name: "common-word-cloud-adv",
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
      .get("http://localhost:5500/wordcloud/posADV")
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