<template>
    <div class="ms-3 text-center">
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="poster"
        @click="goDetail(movie)">
        <p style="color: white;">{{ movie.title }}</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

defineProps({
    movie: Object
})

const goDetail = function(movie) {
    router.push({ name:'detail', params: { id: `${movie.id}` } })
}
</script>

<style scoped>
img {
    transition: transform 0.3s ease;
    width: 150px;
    height: 200px;
}

img:hover {
   transform: scale(1.03);
}
</style>