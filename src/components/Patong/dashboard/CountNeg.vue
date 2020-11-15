<template>
  <div id="count-neg">
    <div class="row">
      <b-col cols="4">
        <p class="head text-center" id="comment-icon">
          <i class="fa fa-minus-circle" style="color: red"></i>
        </p>
      </b-col>

      <b-col cols="6">
        <p class="head text-center magin" id="text">Negative Comments</p>
        <p class="lead text-center magin" id="numComment">
          {{ countNeg }} 
        </p>
        <h3 class=" text-center "> ( {{percenNeg}}% )</h3>
      </b-col>
    </div>
  </div>
</template>

<script>
export default {
  name: "count-neg",
  props: { countNeg: Number, percenNeg: Number },
 
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
  font-size: 30px;
  padding-top: 0;
}
#comment-icon {
  margin-left: 20px;
  font-size: 40px;
  margin-top: 10px;
  margin-right: 20px;
}
.magin{
  margin-bottom: 6px;
}

i.fa {
  display: inline-block;
  border-radius: 60px;
  box-shadow: 0px 0px 5px rgb(248, 0, 0);
  padding: 0.6em 0.6em;
}
</style>