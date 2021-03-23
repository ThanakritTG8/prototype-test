<template>
  <div>
    <canvas id="adv" width="400" height="250"></canvas>
  </div>
</template>
<script>
export default {
  mounted() {
    var text = [];
    var datas = [];
    var label = [];
    this.$axios.get("http://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/patong/topten/negADV.json").then(({ data }) => {
      for (const key in data) {
        if (key > 0) {
          text.push(data[key]);
        }
      }

      for (const key in text) {
        for (let index = 0; index < 1; index++) {
          label.push(text[key][0]);
          datas.push(text[key][1]);
        }
      }
      var ctx = document.getElementById("adv").getContext("2d");
      var myChart = new Chart(ctx, {
        type: "horizontalBar",
        data: {
          labels: label,
          datasets: [
            {
              data: datas,
              backgroundColor: "rgba(255, 127, 15, 0.49)",

              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          legend: {
            display: false,
          },
          title: {
            display: true,
            text: "Adverb",
            fontSize: 20,
          },
        },
      });
    });
  },
  data: () => ({}),
};
</script>