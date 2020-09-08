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
    name:"null",
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
      { word: "สงบ", count: 13 },
      { word: "ลาก", count: 1 },
      { word: "แสน", count: 1 },
      { word: "อบอุ่น", count: 1 },
      { word: "สุภาพ", count: 8 },
      { word: "ไม่สกปรก", count: 9 },
      { word: "ภายหลัง", count: 1 },
      { word: "อีกครั้ง", count: 13 },
      { word: "ตลอดเวลา", count: 1 },
      { word: "สะดวก", count: 14 },
      { word: "ไม่สกปรก", count: 15 },
      { word: "อย่างดี", count: 10 },
      { word: "ค่อนข้างจะ", count: 1 },
      { word: "ถูกต้อง", count: 8 },
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