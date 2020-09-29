<template>
  <div id="count-neg">
    <div class="row">
      <div class="col-lg-6">
        <p class="head text-left" id="comment-icon">
          <i class="fa fa-minus-circle" style="color: red"></i>
        </p>
      </div>

      <div class="col-lg-5">
        <p class="head" id="text">Negative Comment</p>
        <p class="lead" id="numComment" v-for="datas in data" :key="datas">
          {{ datas.numComment }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "count-neg",
  data: () => ({
    data: undefined,
  }),
  mounted() {
    var arr = [];
    this.$axios.get("http://localhost:5000/counts/neg").then(({ data }) => {
      this.data = data;
    });
  },
};
</script>

<style scoped>
#count-comment {
  font-family: "Lato", Arial, sans-serif;
  text-transform: uppercase;
  width: 100%;
}
#text {
  padding-top: 0px;
  font-size: 15px;
  margin-right: 5px;
}
#numComment {
  font-size: 45px;
  padding-top: 0;
  margin-right: 20px;
}
#comment-icon {
  margin-left: 20px;
  font-size: 40px;
  margin-top: 10px;
  margin-right: 20px;
}

i.fa {
  display: inline-block;
  border-radius: 60px;
  box-shadow: 0px 0px 5px rgb(248, 0, 0);
  padding: 0.6em 0.6em;
}
</style>