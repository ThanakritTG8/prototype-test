<template>
  <div id="count-comment">
    <div class="row">
      <b-col cols="4" class=" text-center">
        <p id="comment-icon">
          <i class="fa fa-comments"></i>
        </p>
      </b-col>
      <b-col cols="6">
        <p class="head text-center" id="text">All Comments</p>
        <p
          class="lead text-center"
          id="numComment"
          v-for="datas in data"
          :key="datas"
        >
          {{ datas.numComment }}
        </p>
      </b-col>
    </div>
  </div>
</template>

<script>
export default {
  name: "count-comment",
  data: () => ({
    data: undefined,
  }),
  mounted() {
    this.$axios.get("http://localhost:5500/counts/all").then(({ data }) => {
      this.data = data;
    });
  },
};
</script>

<style scoped>
#count-comment {
  font-family: "Lato", Arial, sans-serif;
  
  width: 100%;
}

#text {
  padding-top: 0px;
  font-size: 15px;
}

#numComment {
  font-size: 45px;
  padding-top: 0;
}

#comment-icon {
  font-size: 40px;
  margin-top: 10px;
}

i.fa {
  display: inline-block;
  border-radius: 60px;
  box-shadow: 0px 0px 5px rgb(5, 5, 5);
  padding: 0.6em 0.6em;
}
</style>
