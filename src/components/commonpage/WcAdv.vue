<template>
  <div>
    <h4 class="text-center">Place</h4>
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
 {
   words: "แน่นอน",
   counts: 8
 },
 {
   words: "เงียบ",
   counts: 5
 },
 {
   words: "ยอดเยี่ยม",
   counts: 7
 },
 {
   words: "สวยงาม",
   counts: 7
 },
 {
   words: "เยี่ยม",
   counts: 9
 },
 {
   words: "เสมอ",
   counts: 5
 },
 {
   words: "ใกล้",
   counts: 4
 },
 {
   words: "เรียบร้อย",
   counts: 3
 },
 {
   words: "สูง",
   counts: 1
 },
 {
   words: "รวดเร็ว",
   counts: 4
 },
 {
   words: "อีกครั้ง",
   counts: 2
 },
 {
   words: "สบาย",
   counts: 6
 },
 {
   words: "สะดวก",
   counts: 8
 },
 {
   words: "มหัศจรรย์",
   counts: 10
 },
 {
   words: "เหลือเชื่อ",
   counts: 6
 },
 {
   words: "สุภาพ",
   counts: 5
 },
 {
   words: "ก้าวร้าว",
   counts: 4
 },
 {
   words: "สกปรก",
   counts: 4
 },
 {
   words: "พิเศษ",
   counts: 5
 },
 {
   words: "ธรรมดา",
   counts: 2
 },
 {
   words: "พลุกพล่าน",
   counts: 7
 },
 {
   words: "สาย",
   counts: 2
 },
 {
   words: "จึง",
   counts: 1
 },
 {
   words: "ก่อน",
   counts: 1
 },
 {
   words: "เพียงแค่",
   counts: 1
 },
 {
   words: "แหลม",
   counts: 1
 },
 {
   words: "โดยเฉพาะอย่างยิ่ง",
   counts: 1
 },
 {
   words: "ลง",
   counts: 1
 },
 {
   words: "จุดสูงสุด",
   counts: 2
 },
 {
   words: "จากนั้น",
   counts: 1
 },
 {
   words: "ต่อไป",
   counts: 1
 },
 {
   words: "ชัด",
   counts: 1
 },
 {
   words: "เกี่ยวกับ",
   counts: 2
 },
 {
   words: "ชม",
   counts: 1
 },
 {
   words: "เหลือเชื่อ",
   counts: 1
 },
 {
   words: "เกินไป",
   counts: 2
 },
 {
   words: "เสมอ",
   counts: 1
 },
 {
   words: "เพียง",
   counts: 1
 },
 {
   words: "นาน",
   counts: 2
 },
 {
   words: "พอ",
   counts: 2
 }
],
  }),
  methods: {
    wordClickHandler(word, count, vm) {
      console.log("wordClickHandler", name, value, vm);
    },
  },
};
</script>
