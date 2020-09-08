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
  name: "common-word-cloud-adj",
  components: {
    wordcloud,

  },

  data: () => ({
    name:"null",
    defaultWords: [
      { word: "ไม่สะอาด ", count: 2 },
      { word: "แน่นอน", count: 3 },
      { word: "แย่", count: 2 },
      { word: "ไม่อร่อย", count: 1 },
      { word: "ไกล", count: 1 },
      { word: "สกปรก", count: 13 },
      { word: "น่ากลัว", count: 1 },
      { word: "เสมอ", count: 1 },
      { word: "มหัศจรรย์", count: 1 },
      { word: "ดัง", count: 13 },
      { word: "ลาก", count: 1 },
      { word: "แสน", count: 1 },
      { word: "อบอุ่น", count: 1 },
      { word: "ก้าวร้าว", count: 8 },
      { word: "สกปรก", count: 9 },

      { word: "อีกครั้ง", count: 1 },
      { word: "ตลอดเวลา", count: 1 },
      { word: "ลำบาก", count: 14 },
      { word: "ไม่สะอาด", count: 15 },
      { word: "ไม่ดี", count: 10 },
      { word: "ค่อนข้างจะ", count: 1 },
      { word: "ผิด", count: 8 },
    ],
  }),
 methods: {
    wordClickHandler(name) {
      this.name = name;
    },
  },
};
</script>
<style  scoped>
.wordcloud {
  height: 250px;
}
</style>