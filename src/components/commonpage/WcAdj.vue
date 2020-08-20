<template>
  <div>
    <h4 class="text-center">Emotion</h4>
    <wordcloud
      class="wordcloud"
      :data="defaultWords"
      nameKey="words"
      valueKey="counts"
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
      { word: "สะอาด", count: 8},
      { word: "ไม่สกปรก", count: 1},
      { word: "ดี", count: 6},
      { word: "ใส", count: 5},
      { word: "สด", count: 4},
      { word: "อร่อย", count: 3 },
      { word: "สูบบุหรี่", count: 2 },
      { word: "แพง", count: 1 },
      { word: "ธรรมดา", count: 1 },
      { word: "เครื่องดื่ม", count: 1 },
      { word: "บาร์", count: 1 },
      { word: "โรแมนติก", count: 1 },
      { word: "ไม่เหม็น", count: 1 },
      { word: "ขาว", count: 1 },
      { word: "สวยงาม", count: 1 },
      { word: "พลุกพล่าน", count: 1 },
      { word: "พิเศษ", count: 1 },
      { word: "วิเศษ", count: 1 },
      { word: "สวย", count: 1 },
      { word: "เชือก", count: 1 },
      { word: "เป็นมิตร", count: 1 },
      { word: "ความสุข", count: 1 },
      { word: "อิ่ม", count: 2},
      { word: "กว้าง", count: 12 },
      { word: "เงียบ", count: 5 },
      { word: "สุภาพ", count: 4 },
      { word: "เรียบร้อย", count: 6 },

      
    ],
  }),
  methods: {
    wordClickHandler(word, count, vm) {
      console.log("wordClickHandler", name, value, vm);
    },
  },
};
</script>
<style  scoped>
.wordcloud{
  height: 250px;
}
</style>