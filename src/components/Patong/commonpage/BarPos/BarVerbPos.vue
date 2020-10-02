<template>
  <div>
    <canvas id="verb" width="400" height="250"></canvas>
  </div>
</template>
<script>
export default {
  mounted() {
    var text = [];
    var datas = [];
    var label = [];
    this.$axios
      .get("http://api.playz-th.com:5500/topten/posVERB")
      .then(({ data }) => {
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
        var ctx = document.getElementById("verb").getContext("2d");
        var myChart = new Chart(ctx, {
          type: "horizontalBar",
          data: {
            labels: label,
            datasets: [
              {
                data: datas,
                backgroundColor: "rgba(0, 230, 46, 0.77)",

                borderColor: "#66CC00",

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
              text: "ACtion",
              fontSize: 20,
            },
          },
        });
      });
  },
};
</script>