<template>
<div id="app">
    <nav-bar></nav-bar>
    <router-view />
</div>
</template>

<script>
import NavBar from '@/layout/NavBar'
export default {
    name: 'App',
    components: {
        NavBar
    }
}
</script>

<style>
#app {
    font-family: 'Quattrocento', serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
}
</style>
