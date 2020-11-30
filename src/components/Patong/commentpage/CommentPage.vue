<template>
  <div id="comment-page">
    <NavBar />

    <b-tabs content-class="mt-3" class="margin">
    
      <b-tab title="All Comments" active>
        <div class="padding">
            <select v-model="month" @change="refes()">
        <option disabled value="">Month</option>
        <option value="January">January</option>
        <option value="February">February</option>
        <option value="March">March</option>
        <option value="April">April</option>
        <option value="May">May</option>
        <option value="June">June</option>
        <option value="July">July</option>
        <option value="August">August</option>
        <option value="September">September</option>
        <option value="Octerber">Octerber</option>
        <option value="November">November</option>
        <option value="December">December</option>
        <option value="">All</option>
      </select>
      <select v-model="year" @change="refes()">
        <option disabled value=''>Year</option>
        <option value="2020">2020</option>
        <option value="2019">2019</option>
        <option value="2018">2018</option>
        <option value="">All</option>
      </select>
          <AllComment :year="year" :month="month" v-if="renderComponent" />
        </div>
      </b-tab>

      <b-tab title="Positive">
        <div class="padding">
          <PositiveComment />
        </div>
      </b-tab>
      <b-tab title="Negative">
        <div class="padding">
          <NegativeComment  />
        </div>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import NegativeComment from "@/components/Patong/commentpage/NegativeComment";
import PositiveComment from "@/components/Patong/commentpage/PositiveComment";
import AllComment from "@/components/Patong/commentpage/AllComment";
import NavBar from "@/layout/NavBar";
export default {
  name: "comment-page",
  components: {
    AllComment,
    NavBar,
    PositiveComment,
    NegativeComment,
  },
  data: () => ({
    month:'',
    year: '',
    renderComponent: true,
  }),
  methods: {
    refes() {
      this.renderComponent = false;

      this.$nextTick(() => {
        // Add the component back in
        this.renderComponent = true;
      });
    },
  },
};
</script>

<style scoped>
.card {
  border-radius: 20px;
}
#body-comment-page {
  margin-top: 100px;
}
h1 {
  margin: 40px;
}
.padding {
  padding: 40px;
}
.margin {
  margin: 30px;
}
</style>