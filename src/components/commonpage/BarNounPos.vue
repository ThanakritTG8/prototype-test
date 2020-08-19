<template>
  <div>
    <apexchart width="500" type="bar" :options="options" :series="series"></apexchart>
  </div>
</template>
<script>
export default {
  data: () => ({
    options: {
      chart: {
        id: "vuechart-example",
      },
      colors: ["#66CC00"],
      title: {
        text: "NOUN",
        align: "center",
        margin: 10,
        style: {
          fontSize: "18px",
          fontWeight: "bold",
          fontFamily: undefined,
           color: "#000",
        },
      },
      xaxis: {
        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
      },
    },
    series: [
      {
        name: "series-1",
        data: [30, 40, 45, 50, 49, 60, 70, 91],
      },
    ],
  }),
};
</script>