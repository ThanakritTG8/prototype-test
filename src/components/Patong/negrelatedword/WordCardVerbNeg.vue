<template>
  <div id="word-card-verb-neg">
    <b-tab v-for="(arrs, ind) in arrData" :key="arrs" :title="arrs">
      <div class="scroll" id="frame">
        <div class="row">
          <div
            class="col-lg-3"
            v-for="items in itemData[ind].sentence"
            :key="items"
          >
            <div class="card shadow p-3 mb-5 bg-white rounded" id="body">
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
  name: "word-card-verb-neg",
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
  /* height: 150px; */
  height: auto;
  /* width: 300px; */
}
</style>
