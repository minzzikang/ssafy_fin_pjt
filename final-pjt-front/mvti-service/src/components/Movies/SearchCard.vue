<template>
    <div @click="goDetail(movie)">
        <img :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`" alt="poster">
        <p class="fw-bold text-white text-center">{{ movie.title }}</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goDetail = function(movie) {
    router.push({ name:'detail', params: { id: `${movie.id}` } })
}

defineProps({
    movie: Object,
})

</script>

<style scoped>

img {
    transition: transform 0.3s ease;
    max-width: 200px;
    height: 300px;
    margin: 10px;
}

img:hover {
   transform: scale(1.03);
}
</style>