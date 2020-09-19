<template>
<div>
    <b-navbar toggleable="lg" type="dark" variant="info" id="home">
        <b-navbar-brand href="#">
            <h3>
                <b>Detect Word Sense</b>
            </h3>
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <router-link to="/" class="navbar" id="font">
                    <div class="navlink">
                        <i class="fas fa-desktop" id="icon"></i>
                        <span>Dashboard</span>
                    </div>
                </router-link>
            </b-navbar-nav>
            <b-navbar-nav>
                <router-link to="/comment" class="navbar" id="font">
                    <div class="navlink">
                        <i class="fas fa-table" id="icon"></i>
                        <span>Comment</span>
                    </div>
                </router-link>
            </b-navbar-nav>
            <b-navbar-nav>
                <router-link to="/common" class="navbar" id="font">
                    <div class="navlink">
                        <i class="fas fa-comments" id="icon"></i>
                        <span>Common Word</span>
                    </div>
                </router-link>
            </b-navbar-nav>
            <b-navbar-nav>
                <router-link to="/related" class="navbar" id="font">
                    <div class="navlink">
                        <span>Related Word</span>
                    </div>
                </router-link>
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <b-nav-form>
                    <b-dropdown id="dropdown-1" text="Place" class="m-md-2">
                        <b-dropdown-item>
                            <router-link to="/">Patong</router-link>
                        </b-dropdown-item>
                        <b-dropdown-item>
                            <router-link to="/dashboard/karon">Karon</router-link>
                        </b-dropdown-item>
                    </b-dropdown>
                </b-nav-form>
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

h3 {
    color: white;
    text-shadow: 2px 2px 4px #000000;
}
</style>
