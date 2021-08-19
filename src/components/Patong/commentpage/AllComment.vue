<template>
  <div id="all-comment">
    <!-- <text-highlight :queries="queries">{{ item }}</text-highlight> -->
    <b-overlay :show="busyLine" rounded="lg" opacity="0.6">
      <b-container fluid>
        <!-- User Interface controls -->

        <b-row>
          <b-col lg="6" class="my-1">
            <b-form-group
              label="Sort"
              label-cols-sm="3"
              label-align-sm="right"
              label-size="sm"
              label-for="sortBySelect"
              class="mb-0"
            >
              <b-input-group size="sm">
                <b-form-select
                  v-model="sortBy"
                  id="sortBySelect"
                  :options="sortOptions"
                  class="w-75"
                >
                  <template v-slot:first>
                    <option value>-- none --</option>
                  </template>
                </b-form-select>
                <b-form-select
                  v-model="sortDesc"
                  size="sm"
                  :disabled="!sortBy"
                  class="w-25"
                >
                  <option :value="false">Asc</option>
                  <option :value="true">Desc</option>
                </b-form-select>
              </b-input-group>
            </b-form-group>
          </b-col>

          <b-col lg="5" class="my-1">
            <b-form-group
              label="Filter"
              label-cols-sm="3"
              label-align-sm="right"
              label-size="sm"
              label-for="filterInput"
              class="mb-0"
            >
              <b-input-group size="sm">
                <b-form-input
                  autocomplete="off"
                  v-model="filter"
                  type="search"
                  id="filterInput"
                  placeholder="Search"
                  @click="filter = ''"
                ></b-form-input>
                <b-input-group-append>
                  <!-- ref="submitBtn" เซตให้ auto click เพื่อ รีเซ็ตค่า fillter ตั้งแต่ รีโหลดหน้า (ทำงานใน mounted)-->
                  <b-button
                    :disabled="!filter"
                    @click="filter = ''"
                    ref="submitBtn"
                    >Clear</b-button
                  >
                </b-input-group-append>
              </b-input-group>
            </b-form-group>
          </b-col>
          <b-col lg="1"></b-col>

          <b-col sm="5" md="6" class="my-1">
            <b-form-group
              label="Per page"
              label-cols-sm="6"
              label-cols-md="4"
              label-cols-lg="3"
              label-align-sm="right"
              label-size="sm"
              label-for="perPageSelect"
              class="mb-0"
            >
              <b-form-select
                v-model="perPage"
                id="perPageSelect"
                size="sm"
                :options="pageOptions"
              ></b-form-select>
            </b-form-group>
          </b-col>

          <b-col sm="6" md="5" class="my-1">
            <b-pagination
              v-model="currentPage"
              :total-rows="totalRows"
              :per-page="perPage"
              align="fill"
              size="sm"
              class="my-0"
            ></b-pagination>
          </b-col>
          <b-col sm="1" md="1" class="my-1"></b-col>
        </b-row>
        <!-- :filter="(filter || '[]') && year" -->
        <div id="space"></div>
        <div class="card">
          <div class="card-body">
            <!-- Main table element -->
            <b-table
              show-empty
              small
              stacked="md"
              :items="item"
              :fields="fields"
              :current-page="currentPage"
              :per-page="perPage"
              :filter="filter"
              :filterIncludedFields="filterOn"
              :sort-by.sync="sortBy"
              :sort-desc.sync="sortDesc"
              :sort-direction="sortDirection"
              @filtered="onFiltered"
            >
              <template #cell(Review)="data">
                <text-highlight :queries="filter">{{
                  data.item.Review
                }}</text-highlight>
              </template>
            </b-table>
          </div>
        </div>
      </b-container>
    </b-overlay>
  </div>
</template>

<script>
export default {
  props: { year: String, month: String },
  data() {
    return {
      busyLine: true,

      item: [],
      fields: [
        {
          key: "Review",
          label: "Reviews",
          sortable: true,
          sortDirection: "desc",
        },
        {
          key: "Rating",
          label: "Rating",
          sortable: true,
          class: "text-center",
        },
        {
          key: "Time",
          label: "Time",
          class: "text-center",
        },
      ],
      totalRows: 0,
      currentPage: null,
      perPage: 5,
      pageOptions: [5, 10, 50],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: [],
      filterOn: [],
      infoModal: {
        id: "info-modal",
        title: "",
        content: "",
      },
    };
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter((f) => f.sortable)
        .map((f) => {
          return { text: f.label, value: f.key };
        });
    },
  },

  mounted() {
    setTimeout(() => {
      this.busyLine = false;
    }, 2000);
    this.$refs.submitBtn.click();
    this.$axios
      .get("https://sentimentanalysis.chochiang.com/tourist/beach/Auto-sentiment-web/API/patong/allcomments.json")
      .then(({ data }) => {
        if (this.year == "" && this.month == "") {
          this.item = data;
        }
        if (this.month != "" && this.year == "") {
          this.item = data.filter((t) => {
            return t.Time.indexOf(this.month) >= 0;
          });
        }
        if (this.month == "" && this.year != "") {
          this.item = data.filter((t) => {
            return t.Time.indexOf(this.year) >= 0;
          });
        }
          if (this.month != "" && this.year != "") {
            const time = this.month+' '+this.year;
          this.item = data.filter((t) => {
            return t.Time.indexOf(time) >= 0;
          });
        }

        this.totalRows = this.item.length;
      });
  },
  methods: {
    info(item, index, button) {
      this.infoModal.title = `Row index: ${index}`;
      this.infoModal.content = JSON.stringify(this.item, null, 2);
      this.$root.$emit("bv::show::modal", this.infoModal.id, button);
    },
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
  },
};
</script>

<style scoped>
#space {
  margin-bottom: 40px;
}
</style>