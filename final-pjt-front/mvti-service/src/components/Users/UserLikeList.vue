<template>
    <div>
        <p>찜한 영화</p>
        <div class="d-flex">
            <UserLikeCard
            v-for="movie in userLikeMovie"
            :key="movie.id"
            :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import UserLikeCard from '@/components/Users/UserLikeCard.vue'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'

const movieStore = useMovieStore()
const userStore = useUserStore()

const userLikeMovie = computed(() => {
    return movieStore.movies.filter(movie => {
        return movie.movie_like_users.includes(userStore.user.pk);
    })
})

</script>

<style scoped>

</style>