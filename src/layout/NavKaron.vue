<template>
<div>
    <b-navbar toggleable="lg" type="dark" variant="info" id="home">
        <b-navbar-brand href="#" content="Automatic Tourism sentiment analysis" v-tippy="{ placement : 'top',  arrow: true }">
           <img src="../assets/atsa4.png" alt="" id="img">
            
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <router-link to="/dashboard/karon" class="navbar" id="font">
                    <div class="navlink">
                        <i class="fas fa-desktop" id="icon"></i>
                        <span>Dashboard</span>
                    </div>
                </router-link>
            </b-navbar-nav>
            <b-navbar-nav>
                <router-link to="/comment/karon" class="navbar" id="font">
                    <div class="navlink">
                        <i class="fas fa-table" id="icon"></i>
                        <span>Reviews</span>
                    </div>
                </router-link>
            </b-navbar-nav>
            <b-navbar-nav>
                <router-link to="/common/karon" class="navbar" id="font">
                    <div class="navlink">
                        <i class="fas fa-comments" id="icon"></i>
                        <span>Common Word</span>
                    </div>
                </router-link>
            </b-navbar-nav>
            <b-navbar-nav>
                <router-link to="/related/karon" class="navbar" id="font">
                    <div class="navlink">
                        <i class="fas fa-link" id="icon"></i>
                        <span>Related Word</span>
                    </div>
                </router-link>
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
             
               <router-link to="/">
          <b-button
            class="button"
            pill
            variant="warning"
            @click="Confirm"
          >
            Place</b-button >
          </router-link>
               
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
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
    font-size: 18px;
    
}

#font {
    color: aliceblue;
}

/* h3 {
    color: white;
    text-shadow: 2px 2px 4px #000000;
} */
#img {
    width: 80px;
}
</style>
