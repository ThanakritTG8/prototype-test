<template>
  <div>
      <h3>Negative</h3><br>
    <canvas id="PieNeg" weight="300" height="300"></canvas>
  </div>
</template>
<script>
export default {
  mounted() {
      var ctx = document.getElementById("PieNeg").getContext("2d");
    var myDoughnutChart = new Chart(ctx, {
      type: "doughnut",
      data: {
          
        datasets: [
          {
            data: [30 , 40 , 26 ,10 ],
          
                backgroundColor: [
                'rgba(255, 46, 70, 0.63)',
                'rgba(255, 127, 15, 0.49)',
                'rgba(255, 248, 36, 0.74)',
                'rgba(0, 230, 46, 0.77)'
               
            ],
          
          }],

        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: ["ADJ", "ADV", "NOUN","VERB"],
      },
    
    });
  },
};
</script>
