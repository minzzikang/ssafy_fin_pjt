<template>
    <div class="container">
        <h3 class="text-white mb-3 mt-3">당신의 친구들이 좋아하는 영화!</h3>
        <div class="d-flex">
            <RecommendAgeCard
                v-for="movie in filteredMovieList"
                :key="movie.id"
                :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import RecommendAgeCard from '@/components/Movies/RecommendAgeCard.vue'
import { ref, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMovieStore } from '@/stores/movie'

const movieStore = useMovieStore()
const userStore = useUserStore()

const checkAge = computed(() => {
    if (userStore.user.age < 20) {
        return '10대'
    } else if (userStore.user.age >= 20 && userStore.user.age < 30) {
        return '20대'
    } else if (userStore.user.age >= 30 && userStore.user.age < 40) {
        return '30대'
    } else if (userStore.user.age >= 40 && userStore.user.age < 50) {
        return '40대'
    } else if (userStore.user.age >= 50) {
        return '50대이상'
    }
    return '' // 연령대를 결정할 수 없는 경우 기본값
})
const ageKeywords = {
    '10대': '애니메이션',
    '20대': '액션',
    '30대': '로맨스',
    '40대': '미스터리',
    '50대이상': '역사'
}

const filteredMovieList = computed(() => {
    const keyword = ageKeywords[checkAge.value]
    return movieStore.movies.filter(movie =>
        movie.genres.some(genre => genre.name === keyword)
    )
})


// for (let i = 0; i < movieStore.movies.length; i++) {
//     if (userStore.user.age < 20) {
//         for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
//             if (movieStore.movies[i].genres[j].name === '애니메이션') {
//                 if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
//                 } else {
//                     movieList.value.push(movieStore.movies[i])
//                 }
//             }
//         }
//     }
//     if (userStore.user.age >= 20 && userStore.user.age < 30) {
//         for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
//             if (movieStore.movies[i].genres[j].name === '액션') {
//                 if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
//                 } else {
//                     movieList.value.push(movieStore.movies[i])
//                 }
//             }
//         }
//     }
//     if (userStore.user.age >= 30 && userStore.user.age < 40) {
//         for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
//             if (movieStore.movies[i].genres[j].name === '로맨스') {
//                 if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
//                 } else {
//                     movieList.value.push(movieStore.movies[i])
//                 }
//             }
//         }
//     }
//     if (userStore.user.age >= 40 && userStore.user.age < 50) {
//         for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
//             if (movieStore.movies[i].genres[j].name === '미스터리') {
//                 if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
//                 } else {
//                     movieList.value.push(movieStore.movies[i])
//                 }
//             }
//         }
//     }
//     if (userStore.user.age >= 50) {
//         for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
//             if (movieStore.movies[i].genres[j].name === '역사') {
//                 if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
//                 } else {
//                     movieList.value.push(movieStore.movies[i])
//                 }
//             }
//         }
//     }
// }
</script>

<style scoped>

</style>