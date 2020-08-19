<template>
  <div>
    <h4 class="text-center">Place</h4>
    <wordcloud
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
    defaultWords: [
         { word: "สะอาด ", count: 2 },
      { word: "แน่นอน", count: 3 },
      { word: "ดี", count: 2 },
      { word: "อร่อย", count: 1 },
      { word: "ห่าง", count: 1 },
      { word: "สวยงาม", count: 1 },
      { word: "ปลอดภัย", count: 1 },
      { word: "เสมอ", count: 1 },
      { word: "มหัศจรรย์", count: 1 },
      { word: "สงบ", count: 1 },
      { word: "ลาก", count: 1 },
      { word: "แสน", count: 1 },
      { word: "อบอุ่น", count: 1 },
      { word: "สุภาพ", count: 1 },
      { word: "สกปรก", count: 1 },
    ],
  }),
  methods: {
    wordClickHandler(word, count, vm) {
      console.log("wordClickHandler", name, value, vm);
    },
  },
};
</script>
