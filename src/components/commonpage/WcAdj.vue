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
        words: "ดี",
        counts: 7,
      },
      {
        words: "เล็ก",
        counts: 5,
      },
      {
        words: "แพง",
        counts: 6,
      },
      {
        words: "สกปรก",
        counts: 9,
      },
      {
        words: "แออัด",
        counts: 10,
      },
      {
        words: "ปลอดภัย",
        counts: 12,
      },
      {
        words: "ตื้น",
        counts: 3,
      },
      {
        words: "กว้าง",
        counts: 1,
      },
      {
        words: "เรียบร้อย",
        counts: 2,
      },
      {
        words: "เก่า",
        counts: 4,
      },
      {
        words: "เงียบ",
        counts: 10,
      },
      {
        words: "ประหลาด",
        counts: 7,
      },
      {
        words: "หยาบคาย",
        counts: 15,
      },
      {
        words: "ส่วนตัว",
        counts: 3,
      },
      {
        words: "ยุ่งเหยิง",
        counts: 12,
      },
      {
        words: "ตื่นเต้น",
        counts: 4,
      },
      {
        words: "ว่าง",
        counts: 2,
      },
      {
        words: "เสียงดัง",
        counts: 9,
      },
      {
        words: "บ้าคลั่ง",
        counts: 15,
      },
      {
        words: "น่าเบื่อ",
        counts: 4,
      },
      {
        words: "มีชื่อเสียง",
        counts: 13,
      },
      {
        words: "อันตราย",
        counts: 3,
      },
      {
        words: "อ่อนโยน",
        counts: 6,
      },
      {
        words: "สดชื่น",
        counts: 4,
      },
      {
        words: "บริสุทธิ์",
        counts: 1,
      },
      {
        words: "ระมัดระวัง",
        counts: 1,
      },
      {
        words: "โล่ง",
        counts: 1,
      },
      {
        words: "สด",
        counts: 1,
      },
      {
        words: "นั่งเล่น",
        counts: 1,
      },
      {
        words: "ร้อน",
        counts: 1,
      },
    ],
  }),
  methods: {
    wordClickHandler(word, count, vm) {
      console.log("wordClickHandler", name, value, vm);
    },
  },
};
</script>
