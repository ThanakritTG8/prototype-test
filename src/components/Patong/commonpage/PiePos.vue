<template>
  <div>
    <center><h3>Positive</h3></center>
    <br />
    <canvas id="Pie" weight="300" height="300"></canvas>
  </div>
</template>
<script>
export default {
  mounted() {
    var datas = [];
    var label = [];
    this.$axios.get("https://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/patong/piechart/pos.json").then(({ data }) => {
      for (const key in data) {
        for (let index = 0; index < 1; index++) {
          datas.push(data[key][1]);
          label.push(data[key][0]);
        }
      }
   
        var ctx = document.getElementById("Pie").getContext("2d");
      var myDoughnutChart = new Chart(ctx, {
        type: "doughnut",
        data: {

          datasets: [
            {
              data: datas,

                  backgroundColor: [
                  'rgba(255, 46, 70, 0.63)',
                  'rgba(255, 127, 15, 0.49)',
                  'rgba(255, 248, 36, 0.74)',
                  'rgba(0, 230, 46, 0.77)'

              ],

            }],

          // These labels appear in the legend and in the tooltips when hovering different arcs
          labels: label,
        },

      });
     });
  },
};
</script>
