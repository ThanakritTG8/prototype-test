<template>
  <div id="home">
    <section class="fullpage">
      <div class="container">
        <center>
          <div >
            <img src="../assets/atsa.png" alt="" width="350" height="350" class="img  "/>
          </div>
          <div>
                    <vue-dropdown 
            style="
              box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                0 6px 20px 0 rgba(0, 0, 0, 0.19);
            "
            :config="config"
            @setSelectedOption="setNewSelectedOption($event)"
          ></vue-dropdown>

          </div>
          <div>
              <b-button
            class="button shadow-lg p-3 mb-5 rounded"
            pill
            variant="warning"
            style="margin-top: 40px"
            @click="Confirm()"
          >
            Confirm</b-button
          >
          </div>
  
        
        </center>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    data: "",
    config: {
      options: [
        {
          value: "Patong",
        },
      ],
      placeholder: "Place",
      backgroundColor: "white",
      width: 180,

      borderRadius: "1.5em",
    },
  }),
  methods: {
    setNewSelectedOption(selectedOption) {
      this.config.placeholder = selectedOption.value;
      this.data = selectedOption.value;
    },
    Confirm() {
      if (!this.data) {
        this.$alert("Please select a place", "warning", "warning");
      } else {
        this.$router.push({ path: "/dashboard" });
      }
    },
  },
};
</script>

<style scoped>
#home {
  background-image: url("../assets/patong.jpg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
button {
  size: 20px;
  width: 150px;
  height: 50px;
}
.img{
margin-top: 60px;
margin-bottom: -60px;
}
/* button:hover{
    size: 20px;
  width: 150px;
  height: 50px;
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
} */
p {
  size: 16px;

  text-shadow: 8px 8px 12px rgb(62, 94, 199);
}
h1 {
  font-family: "Orbitron", sans-serif;
  text-shadow: 8px 8px 12px rgb(62, 94, 199);
}

.fullpage {
  height: 100vh;
  width: 100%;
}
</style>
