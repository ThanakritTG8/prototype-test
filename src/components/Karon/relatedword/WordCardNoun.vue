<template>
  <div id="word-card-noun">
    <b-tab v-for="(arrs, ind) in arrData" :key="arrs" :title="arrs">
      <div class="scroll" id="frame">
        <div class="row">
          <div
            class="col-lg-3 col-md-6 col-sm-12"
            v-for="items in itemData[ind].sentence"
            :key="items"
          >
            <div class="card shadow rounded" id="body">
              <div class="card-body">
                <div class="card-text">
                  <p>{{ items }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </b-tab>
  </div>
</template>

<script>
export default {
  name: "word-card-noun",
  props: ["itemData", "arrData"]
};
</script>

<style scoped>
.b-tab {
  margin-bottom: 20px;
  height: 520px;
  /* height: auto; */
  overflow-y: scroll;
}
#frame {
  height: 500px;
  /* height: auto; */
  overflow-y: scroll;
}
#body {
  margin-bottom: 10px;
  margin-right: 10px;
  /* height: 150px; */
  height: auto;
  /* width: 300px; */
}
</style>
