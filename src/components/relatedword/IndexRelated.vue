<template>
<div id="index-related">
    <h1 v-for="items in item" :key="items">{{ items.tg1 }}</h1>
    {{item}}
    <b-container scrollable>
        <b-row align-v="center">
            <wordcard />
            <wordcard />
            <wordcard />
        </b-row>
    </b-container>
</div>
</template>

<script>
import wordcard from '@/components/relatedword/wordcard'
export default {
    name: 'index-related',
    components: {
        wordcard
    },
    data: () => ({
        item: {
            "tg1": ["tg11", "tg12", "tg13"],
            "tg2": ["tg21", "tg22", "tg23"]
        }

    })
}
</script>

<style>

</style>
