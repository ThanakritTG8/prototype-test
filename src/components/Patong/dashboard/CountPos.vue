<template>
  <div id="count-pos">
    <div class="row">
      <b-col cols="4">
        <p class="head text-center" id="comment-icon">
          <i class="fa fa-plus-circle" style="color:rgb(85, 253, 139)"></i>
        </p>
      </b-col>
     <b-col cols="6">
        <p class="head text-center magin" id="text">Positive Comments</p>
         <p class="lead text-center magin" id="numComment">{{ countPos }}</p>
         <h3 class=" text-center"> ( {{percenPos}}% )</h3>
     </b-col>
    </div>
  </div>
</template>

<script>
export default {
  name: "count-pos",
  props: {countPos:Number, percenPos:Number},
  
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
 
}
.magin{
  margin-bottom: 6px;
}

i.fa {
  display: inline-block;
  border-radius: 60px;
  box-shadow: 0px 0px 5px rgb(85, 253, 139);
  padding: 0.6em 0.6em;
}
</style>