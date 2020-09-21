<template>
<div id="wordcard">
    <b-col cols="4">
        <b-card id="frame">
            <p class="title">TG</p>
            <b-card class="scroll" align-v="left">
                <b-card class="card" align-v="left">
                    <b-card-body>
                        <b-card-text>Card Title</b-card-text>
                    </b-card-body>
                </b-card>
            </b-card>
        </b-card>
    </b-col>
    {{item}}
</div>
</template>

<script>
export default {
    data: () => ({
        item: undefined
    }),
     mounted() {

        this.$axios
            .get("http://localhost:5000/senten/text/NOUN")
            .then(({ data }) => {             
                this.item = data;
                console.log(this.item);
            });
            
    },
}
</script>

<style>
#word-card {
    margin-top: 50px ;
}
.scroll {
    width: 300px;
    height: 500px;
    overflow-y: scroll;
}

.card {
    background: whitesmoke;
    margin-top: 20px;
}
#frame {
    width: 350px;
}
</style>
