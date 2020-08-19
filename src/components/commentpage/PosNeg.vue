<template>
  <div id="pos-neg">
    <h3>All Positive and Negative</h3>
    <canvas id="pie"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

export default {
  name: "date",
  data: () => ({}),
  mounted: function () {
    var ctx = document.getElementById("pie").getContext("2d");
    var line = new Chart(ctx, {
      type: "pie",
      data: {
        labels: ['Positive', 'Negative'],
        datasets: [
          {
            data: [1800, 1200],
            backgroundColor: ['#77f078', '#ff3449']
          }
        ],
      },
      options: {
        responsive: true,
      },
    });
  },
};
</script>

<style>
</style>