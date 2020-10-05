<template>
  <div id="home">
    <section class="fullpage">
      <div class="container">
        <center>
          <br />
          <h1 style="margin-top: 100px">Detect Word Sense</h1>
          <p class="card-text">Automatic Tourism Sentiment Analysis</p>

          <vue-dropdown
            style="
              margin-top: 80px;
              box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2),
                0 6px 20px 0 rgba(0, 0, 0, 0.19);
            "
            :config="config"
            @setSelectedOption="setNewSelectedOption($event)"
          ></vue-dropdown>
          <router-link to="/dashboard">
            <b-button
              class="button"
              pill
              variant="warning"
              style="margin-top: 40px"
              @click="Confirm"
            >
              Confirm</b-button
            >
          </router-link>
        </center>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    showDB: false,
    show: true,
    config: {
      options: [
        {
          value: "Patong",
        },
        {
          value: "Karon",
        },
      ],
      placeholder: "Place",
      backgroundColor: "white",
      width: 180,
    },
  }),
  methods: {
    setNewSelectedOption(selectedOption) {
      this.config.placeholder = selectedOption.value;
    },
    Confirm() {
      this.show = false;
      this.showDB = true;
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
