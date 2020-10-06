<template>
  <div id="count-pos">
    <div class="row">
      <b-col cols="6">
        <p class="head text-center" id="comment-icon">
          <i class="fa fa-plus-circle" style="color:rgb(85, 253, 139)"></i>
        </p>
      </b-col>
     <b-col cols="4">
        <p class="head text-center" id="text">Positive Comment</p>
         <p class="lead text-center" id="numComment"
            v-for="datas in data" :key="datas">{{ datas.numComment }}</p>
     </b-col>
    </div>
  </div>
</template>

<script>
export default {
  name: "count-pos",
  data: () => ({
        data: undefined
    }),
    mounted() {
      var arr =[]
        this.$axios
            .get("http://localhost:5500/counts/pos")
            .then(({ data }) => { 
             this.data=data
                
            });
    },
}
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
  
}
#numComment {
  font-size: 45px;
  padding-top: 0;
  
}
#comment-icon {
  margin-left: 20px;
  font-size: 40px;
  margin-top: 10px;
 
}

i.fa {
  display: inline-block;
  border-radius: 60px;
  box-shadow: 0px 0px 5px rgb(85, 253, 139);
  padding: 0.6em 0.6em;
}
</style>