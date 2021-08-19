<template>
  <div id="date">
    <p class="title">Monthly Comments</p>
    <canvas id="line" ></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

export default {
  name: "date",
  data: () => ({}),
  mounted: function () {
   
    var labelA = [];
    var color = ["#FF0066","#FF9900","#FFFF00"];
    var ctx = document.getElementById("line").getContext("2d");
    this.$axios.get("https://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/karon/year.json").then(({ data }) => {
      for (let index = 0; index < data.length; index++) {
        for (let indexs = 0; indexs < 1; indexs++) {
              
          var la = {
            label: data[index][0],
            data: data[index][1],
            borderColor: color[index],
            fill: false,
          };
          labelA.push(la)
        }
        console.log(labelA);
      }

      var line = new Chart(ctx, {
        type: "line",
        data: {
          labels: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
          ],
          datasets: labelA,
        },
        options: {
          responsive: true,
        },
      });
    });
  },
};
</script>

<style scoped>

</style>