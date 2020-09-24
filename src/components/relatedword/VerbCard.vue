<template>
  <div id="verb-card">
    <b-container scrollable>
      <b-row align-v="center">
        <!-- // num เพื่อ ใช้วนหาค่าใน item   -->
        <b-col cols="4" v-for="num in arr" :key="num">
          <!-- // รูปแบบ joson [{"ชาย": [arr] }]  -->
          <div
            class="card"
            v-for="(items, index) in item[num]"
            :key="index"
            id="frame"
            :per-page="perPage"
            :current-page="currentPage"
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
        </b-col>
      </b-row>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        first-text="First"
        prev-text="Prev"
        next-text="Next"
        last-text="Last"
        aria-controls="frame"
      ></b-pagination>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "verb-card",
  components: {
    
  },
  data: () => ({
    item: undefined,
    arr: [],
    getRows:undefined,
    currentPage:1,
    perPage:3
  }),
  mounted() {
    this.$axios
      .get("http://localhost:5000/senten/text/test/VERB")
      .then(({ data }) => {
        this.item = data;
        for (const key in data) {
          this.arr.push(key);
        }
      });
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
#frame {
  width: 340px;
}
.card {
  background: whitesmoke;
  margin-top: 20px;
  margin-right: 10px;
}
</style>
