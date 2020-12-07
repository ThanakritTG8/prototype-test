<template>
  <div class="dashboard">
    <NavKaron/>
    <index-dashboard/>
  </div>
</template>

<script>
import IndexDashboard from '@/components/Karon/dashboard/IndexDashboard'
import NavKaron from "@/layout/NavKaron";
export default {
  name: "dashboard",
  components: {
    IndexDashboard,
    NavKaron
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
