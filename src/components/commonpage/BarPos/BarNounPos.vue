<template>
  <div>
    <canvas id="myChart" width="400" height="250"></canvas>
    {{ data }}
  </div>
</template>
<script>
export default {
  data: () => ({}),
  mounted() {
    var text = [];
    var datas = [];
    var label = [];
    this.$axios
      .get("http://localhost:5000//topten/posNOUN")
      .then(({ data }) => {
        for (const key in data) {
          if (key > 0) {
            text.push(data[key]);
          }
        }
        for (const key in text) {
          for (let index = 0; index < 1; index++) {
            label.push(text[key][0]);
            datas.push(text[key][1]);
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
                backgroundColor: "rgba(255, 248, 36, 0.74)",

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
              fontSize: 20,
            },
          },
        });
      });
  },
};
</script>