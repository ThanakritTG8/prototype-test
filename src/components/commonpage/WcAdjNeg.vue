<template>
  <div>
    <h4 class="text-center">Emotion</h4>
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
      { word: "สกปรก", count: 8 },
      { word: "ไม่สะอาด", count: 1 },
      { word: "แย่", count: 6 },
      { word: "ขุ่น", count: 5 },
      { word: "สด", count: 4 },
      { word: "ไม่อร่อย", count: 3 },
      { word: "สูบบุหรี่", count: 2 },
      { word: "แพง", count: 1 },
      { word: "ธรรมดา", count: 1 },
      { word: "อาหาร", count: 1 },
      { word: "บาร์", count: 1 },
      { word: "โรแมนติก", count: 1 },
      { word: "เหม็น", count: 1 },
      { word: "ดำ", count: 1 },
      { word: "น่าเกลียด", count: 8 },
      { word: "พลุกพล่าน", count: 1 },
      { word: "ไม่พิเศษ", count: 1 },
      { word: "ไม่วิเศษ", count: 1 },
      { word: "ไม่สวย", count: 1 },
      { word: "เชือก", count: 1 },
      { word: "ไม่เป็นมิตร", count: 1 },
      { word: "ความสุข", count: 1 },
      { word: "อิ่ม", count: 2 },
      { word: "แคบ", count: 12 },
      { word: "ดัง", count: 5 },
      { word: "ไม่เรียบร้อย", count: 6 },
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