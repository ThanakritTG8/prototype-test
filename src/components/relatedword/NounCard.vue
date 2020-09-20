<template>
<div id="noun-card">
    <!-- <p v-for="items in item" :key="items">{{  }}</p> -->
    <b-container scrollable>
        <b-row align-v="center">
            <wordcard />
        </b-row>
    </b-container>
    
</div>
</template>

<script>
import wordcard from '@/components/relatedword/wordcard'
export default {
    name: 'noun-card',
    components: {
        wordcard
    },
}
</script>

<style>
#noun-card {
    margin-top: 40px;
}
</style>
