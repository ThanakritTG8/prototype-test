<template>
  <div>
    <canvas id="verb" width="400" height="250"></canvas>
  </div>
</template>
<script>
export default {
  mounted() {
    var text=[[ "มี", 34 ], [ "สามารถ", 19 ], [ "จะ", 15 ], [ "อยู่", 9 ], [ "ให้", 8 ], [ "เพลิดเพลิน", 8 ], [ "เดิน", 7 ], [ "แออัด", 6 ], [ "ทำ", 6 ], [ "ต้องการ", 6 ] ]
    var datas = []
    var label = []
   for (const key in text) {
     for (let index = 0; index < 1; index++) {
       label.push(text[key][0])
       datas.push(text[key][1])
     }
    }
    var ctx = document.getElementById("verb").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: label,
        datasets: [
          {
            data: datas,
            backgroundColor: 
              "rgba(0, 230, 46, 0.77)",
            
            borderColor: 
              "#66CC00",
            
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
            text: "Action",
            fontSize:20,
          },
       
      },
    });
  },
  data: () => ({}),
};
</script>