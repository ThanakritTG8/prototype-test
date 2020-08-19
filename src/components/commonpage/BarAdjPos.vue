<template>
  <div>
    <canvas id="adj" width="400" height="250"></canvas>
  </div>
</template>
<script>
export default {
  mounted() {
    var text=[[ "ดี", 20 ], [ "มาก", 18 ], [ "ใหญ่", 15 ], [ "สุด", 10  ], [ "น้อย", 9 ], [ "ดัง", 8 ], [ "ไม่แย่", 7 ], [ "ส่วนตัว", 7 ] ,["สวย",5]]
    var datas = []
    var label = []
   for (const key in text) {
     for (let index = 0; index < 1; index++) {
       label.push(text[key][0])
       datas.push(text[key][1])
     }
    }
    var ctx = document.getElementById("adj").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: label,
        datasets: [
          {
            data: datas,
            backgroundColor: 
              "rgba(255, 46, 70, 0.63)",
            
           
            
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
            text: "Emotion",
            fontSize:20,
          },
       
      },
    });
  },
  data: () => ({}),
};
</script>