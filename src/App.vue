<template>
  <div id="app">
    
    <router-view />
  </div>
</template>

<script>import Dashboard from "@/components/dashboard/Dashboard";
import NavBar from "@/layout/NavBar";
export default {
  name: "App",
 
};
</script>

<style scoped>
/* #app {
  background-image: url("https://u01.appmifile.com/images/2019/06/01/7ed90965-208c-4057-a8e0-8cad71ac7400.jpeg ");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
button {
  size: 20px;
  width: 150px;
  height: 50px;
}

p {
  size: 16px;

  text-shadow: 8px 8px 12px rgb(62, 94, 199);
}
h1 {
  font-family: "Orbitron", sans-serif;
  text-shadow: 8px 8px 12px rgb(62, 94, 199);
}

.fullpage {
  height: 120vh;
  width: 100%;
} */
</style>
