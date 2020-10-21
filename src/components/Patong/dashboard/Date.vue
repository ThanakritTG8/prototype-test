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
    var color = ["#FF0066","#FF9900","#FFFF00","#CC0099","#9966FF","#66FFFF","#CBAB8D","#FDB4BF","#FFBE7D","#D0B3E1","#B3B3D9","#6E7EF5"];
    var ctx = document.getElementById("line").getContext("2d");
    this.$axios.get("http://localhost:5500/year").then(({ data }) => {
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