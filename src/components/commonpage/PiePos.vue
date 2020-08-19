<template>
    <div>
          <apexchart width="400" type="donut" :options="options" :series="series"></apexchart>

    </div>
</template>
<script>
export default {
    data:()=>({
 options: {},
       options: {
           labels: ['Apple', 'Mango', 'Orange', 'Watermelon'],
           
       },
      series: [44, 55, 41, 17]
    })
}
</script>