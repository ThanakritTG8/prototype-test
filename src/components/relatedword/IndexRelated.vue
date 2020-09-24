<template>
<div id="index-related">
    <div id="group">
        <h1 class="title text-center">Related Word</h1>
    </div>
    <div>
        <b-tabs content-class="mt-3" fill
            align="center"
            active-nav-item-class="font-weight-bold text-uppercase text-success"
            active-tab-class=""
        >
            <b-tab title="Place" active>    
                <noun-card />
            </b-tab>
            <b-tab title="Action">
                <!-- <noun-card /> -->
            </b-tab>
            <b-tab title="Emotion">
                <!-- <noun-card /> -->
            </b-tab>
            <b-tab title="Character">
                <!-- <noun-card /> -->
            </b-tab>
        </b-tabs>
    </div>
    {{item}}
</div>
</template>

<script>
import NounCard from '@/components/relatedword/NounCard'
import wordcard from '@/components/relatedword/wordcard'
export default {
    name: 'index-related',
    components: {
        wordcard,
        NounCard
    },
    data: () => ({
        item: undefined
    }),
     mounted() {
        this.$axios
            .get("http://localhost:5000/senten/text/test/NOUN")
            .then(({ data }) => { 
                this.item = data;
                console.log(item);
            });
    },
}
</script>

<style>
#group {
    margin-top: 40px;
    margin-bottom: 50px;
}
</style>
