<template>
  <div class="dashboard">
    <index-dashboard/>
  </div>
</template>

<script>
import IndexDashboard from '@/components/dashboard/IndexDashboard'

export default {
  name: "dashboard",
  components: {
    IndexDashboard
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
