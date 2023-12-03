<template>
    <div class="container">
        <h3 class="text-white mb-3 mt-3">{{ season }}에 잘어울리는 영화!</h3>
        <div class="d-flex">
            <RecommendTodayCard 
                v-for="movie in filteredMovies"
                :key="movie.id"
                :movie="movie"
            />
        </div>
    </div>
</template>

<script setup>
import RecommendTodayCard from '@/components/Movies/RecommendTodayCard.vue'
import { ref, computed } from 'vue'
import { useMovieStore } from '@/stores/movie'

const movieStore = useMovieStore()
const movieList = ref([])

// 오늘 월 계산해서 계절별로 영화 추천
const today = new Date()
const month = today.getMonth() + 1

const season = computed(() => {
    if (month >= 3 && month <= 5) {
        return '봄'
    } else if (month >= 6 && month <= 8) {
        return '여름'
    } else if (month >= 9 && month <= 11) {
        return '가을'
    } else {
        return '겨울'
    }
})

const excludeKeywords = {
    '봄': ['홀로', '크리스마스', '눈'],
    '여름': ['해리', '크리스마스', '눈'],
    '가을': ['포레', '티파니', '어벤'],
    '겨울': ['호빗', '킹', '존', '로그']
}

const seasonKeywords = {
    '봄': ['재즈', '사쿠라', '따뜻한'],
    '여름': ['해변', '여름'],
    '가을': ['낭만', '가을', '만남'],
    '겨울': ['크리스마스', '눈이']
}

const filteredMovies = computed(() => {
    return movieStore.movies.filter(movie => {
        const includeKeyword = seasonKeywords[season.value]
        const excludeKeyword = excludeKeywords[season.value]

        // 영화 개요에 포함할 키워드가 있는지 확인
        const includeCheck = includeKeyword.some(keyword => movie.overview.includes(keyword))

        // 영화 제목에 제외할 키워드가 있는지 확인
        const excludeCheck = excludeKeyword.some(keyword => movie.title.includes(keyword))

        // 포함할 키워드가 있고 제외할 키워드가 없는 경우만 필터링
        return includeCheck && !excludeCheck;
    })
})

// for (let i = 0; i < movieStore.movies.length; i++) {
//     if (season.value === '봄') {
//         if (movieStore.movies[i].overview.includes('재즈')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('사쿠라')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('따뜻한')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)
//                 || movieStore.movies[i].title.includes('홀로')
//                 || movieStore.movies[i].title.includes('크리스마스')
//                 || movieStore.movies[i].title.includes('눈')
//             ) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (season.value === '여름') {
//         if (movieStore.movies[i].overview.includes('해변')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('여름')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)
//                 || movieStore.movies[i].title.includes('해리')
//                 || movieStore.movies[i].title.includes('크리스마스')
//                 || movieStore.movies[i].title.includes('눈')
//             ) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (season.value === '가을') {
//         if (movieStore.movies[i].overview.includes('낭만')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//             movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('가을')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('만남')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)
//                 || movieStore.movies[i].title.includes('포레')
//                 || movieStore.movies[i].title.includes('티파니')
//                 || movieStore.movies[i].title.includes('어벤')
//             ) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (season.value === '겨울') {
//         if (movieStore.movies[i].title.includes('겨울')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//             movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('크리스마스')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('눈이')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)
//                 || movieStore.movies[i].title.includes('호빗')
//                 || movieStore.movies[i].title.includes('킹')
//                 || movieStore.movies[i].title.includes('존')
//                 || movieStore.movies[i].title.includes('로그')
//             ) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
// }

</script>

<style scoped>

</style>