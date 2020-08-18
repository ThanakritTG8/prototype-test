<template>
  <div id="nav-bar">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">
        <h4>
          <b>Detect Word Sense</b>
        </h4>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-button v-b-toggle.sidebar-backdrop>
            <b-icon icon="justify" font-scale="1.5"></b-icon>
          </b-button>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <b-sidebar id="sidebar-backdrop" bg-variant="dark" text-variant="light" shadow>
      <router-link to="/" class="navbar">
        <div class="navlink">
          <i class="fas fa-desktop" id="icon"></i>
          <span>Dashboard</span>
        </div>
      </router-link>
      <router-link to="/comment" class="navbar">
        <div class="navlink">
          <i class="fas fa-table" id="icon"></i>
          <span>Comment</span>
        </div>
      </router-link>
      <router-link to="/common" class="navbar">
        <div class="navlink">
          <i class="fas fa-comments" id="icon"></i>
          <span>CommonWord</span>
        </div>
      </router-link>
    </b-sidebar>
  </div>
</template>
<script>
export default {
  name: "nav",
};
</script>

<style scoped>
#home {
  font-weight: 20px;
  font-size: 35px;
}
.title {
  color: #fff;
  font-size: 30px;
  margin-left: 20px;
}
section {
  margin: 30px;
}
#nav {
  background: rgb(70, 72, 129);
}
.navbar {
  width: 100%;
  height: 80px;
  color: #fff;
  font-size: 17px;
}
.navbar:hover {
  background: rgb(88, 255, 163);
}
.navlink {
  margin-left: 20px;
}
#icon {
  margin-right: 20px;
}
.btn {
  background: none;
}
</style>