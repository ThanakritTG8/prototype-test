<template>
  <div>
    <canvas id="myChart" width="400" height="250"></canvas>
  </div>
</template>
<script>
export default {
  mounted() {
    var text=[[ "ชายหาด", 56 ], [ "การ", 16 ], [ "น้ำ", 15 ], [ "สถานที่", 12 ], [ "อาหาร", 10 ], [ "คุณ", 9 ], [ "กิจกรรม", 8 ], [ "เวลา", 8 ], [ "หาด", 7 ], [ "ถนน", 7 ] ]
    var datas = []
    var label = []
   for (const key in text) {
     for (let index = 0; index < 1; index++) {
       label.push(text[key][0])
       datas.push(text[key][1])
     }
    }
    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: label,
        datasets: [
          {
            data: datas,
            backgroundColor: 
              "rgba(255, 248, 36, 0.74)",
            
         
            
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
            text: "Place",
            fontSize:20,
          },
       
      },
    });
  },
  data: () => ({}),
};
</script>