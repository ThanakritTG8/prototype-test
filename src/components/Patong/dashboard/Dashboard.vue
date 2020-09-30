<template>
  <div class="dashboard">
    <NavBar/>
    <index-dashboard/>
  </div>
</template>

<script>
import IndexDashboard from '@/components/Patong/dashboard/IndexDashboard'
import NavBar from "@/layout/NavBar";
export default {
  name: "dashboard",
  components: {
    IndexDashboard,
    NavBar
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
