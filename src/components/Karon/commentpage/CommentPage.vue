<template>
  <div id="comment-page">
    <NavBar />

    <b-tabs content-class="mt-3" class="margin">
      <b-tab title="All Comments" active>
        <div class="padding">
          <b-row class="select">
            <b-col  xl="1" lg="2" md="2" sm="1">
              <b-form-select
                v-model="month"
                :options="optionsMonth"
                @change="refes()"
                size="sm"
                class="mt-3 selected " 
              ></b-form-select>
            </b-col>
            <b-col xl="1" lg="2" md="2" sm="1">
              <b-form-select 
                v-model="year"
                :options="optionsYear"
                @change="refes()"
                size="sm"
                class="mt-3 selected "
              ></b-form-select>
            </b-col>
          </b-row>

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
          <NegativeComment />
        </div>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import NegativeComment from '@/components/Karon/commentpage/NegativeComment'
import PositiveComment from "@/components/Karon/commentpage/PositiveComment";
import AllComment from "@/components/Karon/commentpage/AllComment";
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
    month: "",
    year: "",
    renderComponent: true,
    optionsYear: [
      { value: "", text: "--Year--", disabled: true },
      { value: "2020", text: "2020" },
      { value: "2019", text: "2019" },
      { value: "2018", text: "2018" },
      { value: "2017", text: "2017" },
      { value: "", text: "All" },
    ],
    optionsMonth: [
      { value: "", text: "--Month--", disabled: true },
      { value: "January", text: "January" },
      { value: "February", text: "February" },
      { value: "March", text: "March" },
      { value: "April", text: "April" },
      { value: "May", text: "May" },
      { value: "June", text: "June" },
      { value: "July", text: "July" },
      { value: "August", text: "August" },
      { value: "September", text: "September" },
      { value: "October", text: "October" },
      { value: "November", text: "November" },
      { value: "December", text: "December" },
      { value: "", text: "All" },
    ],
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
.select{
 margin-bottom: 20px;
}
.selected{
  width: 100px;
 
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