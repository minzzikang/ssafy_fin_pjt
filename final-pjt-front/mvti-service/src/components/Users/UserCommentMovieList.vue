<template>
    <div>
        <p>댓글 쓴 영화</p>
        <div class="d-flex">
            <UserCommentMovieCard 
            v-for="movie in userCommentMovie"
            :key="movie.id"
            :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import UserCommentMovieCard from '@/components/Users/UserCommentMovieCard.vue'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'

const movieStore = useMovieStore()
const userStore = useUserStore()
console.log(movieStore.movies)
console.log(userStore.user.username)

const userCommentMovie = computed(() => {
    return movieStore.movies.filter(movie => {
        return movie.moviecomment_set.some(comment => comment.username === userStore.user.username);
    })
})
// console.log(userCommentMovie)
</script>

<style scoped>

</style>