<template>
  <div>
    <canvas id="adv" width="400" height="250"></canvas>
  </div>
</template>
<script>
export default {
  mounted() {
    var text=[[ "มาก", 20 ], [ "ที่สุด", 7 ], [ "มากมาย", 6 ], [ "ก็", 6 ], [ "ไว้", 5 ], [ "ใกล้เคียง", 4 ], [ "น้อย", 3 ], [ "สะอาด", 2 ], [ "ยัง", 2 ], [ "กว่า", 1 ] ]
    var datas = []
    var label = []
   for (const key in text) {
     for (let index = 0; index < 1; index++) {
       label.push(text[key][0])
       datas.push(text[key][1])
     }
    }
    var ctx = document.getElementById("adv").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: label,
        datasets: [
          {
            data: datas,
            backgroundColor: 
              "rgba(255, 127, 15, 0.49)",
            
          
            
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
            text: "Character",
            fontSize:20,
          },
       
      },
    });
  },
  data: () => ({}),
};
</script>