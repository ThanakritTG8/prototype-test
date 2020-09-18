<template>
<div id="index-related">
    <h1>Related Word</h1>
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
    }
}
</script>

<style>

</style>
