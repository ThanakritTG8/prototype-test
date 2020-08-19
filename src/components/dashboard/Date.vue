<template>
  <div id="date">
  <p class="title">Monthly Comments</p>
    <canvas id="line"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

export default {
  name: "date",
  data: () => ({}),
  mounted: function () {
    var ctx = document.getElementById("line").getContext("2d");
    var line = new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        datasets: [
          {
            label: "2019",
            data: [61, 122, 107, 73, 80 ,75 ,45, 99, 250 ,300 ,750 ,350],
            borderColor: "#6E7EF5",
            fill: false,
          },
          {
            label: "2018",
            data: [18, 170, 135, 92, 77 ,80 ,75 ,80 ,60 ,45 ,700 ,250],
            borderColor: "#B277DE",
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
      },
    });
  },
};
</script>

<style scoped>
#line {
    width: 90%;
    height: 370;
}
</style>