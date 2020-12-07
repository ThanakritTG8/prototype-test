<template>
  <div id="noun-card">
    <b-container scrollable>
      <div class="row">
        <!-- // num เพื่อ ใช้วนหาค่าใน item   -->
        <div class="col-lg-4 md-6 sm-12" v-for="num in arrData" :key="num">
          <!-- // รูปแบบ joson [{"ชาย": [arr] }]  -->
          <div
            class="card"
            v-for="(items, index) in itemData[num]"
            :key="index"
          >
            <!-- // ประกาศ index เพื่อ โชว์ค่า key  -->
            <div class="card-body">
              <h4 class="card-title">{{ index }}</h4>
              <div class="card scroll">
                <!-- //วนหาค่า value [{"ชาย": [>>ค่าตรงนี้<<] }]  -->
                <div class="card" v-for="(text, index) in items" :key="index">
                  <div class="card-body">
                    <div class="card-text">
                      {{ text }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </b-container>
    <!-- <b-pagination
      v-if="itemData"
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      first-text="First"
      prev-text="Prev"
      next-text="Next"
      last-text="Last"
      aria-controls="nCard"
    ></b-pagination> -->
  </div>
</template>

<script>
export default {
  name: "noun-card",
  components: {},
  data: () => ({
    // currentPage: 1,
    // perPage: 3
  }),
  props: ["itemData", "arrData"],
  methods: {},
  computed: {
    // rows() {
    //   return this.itemData.length;
    // }
  }
};
</script>

<style scoped>
#noun-card {
  margin-top: 40px;
}
.scroll {
  width: 300px;
  height: 500px;
  overflow-y: scroll;
}
/* #nCard {
  width: 340px;
} */
.card {
  background: whitesmoke;
  margin-top: 20px;
  margin-right: 10px;
  height: auto;
}
</style>
