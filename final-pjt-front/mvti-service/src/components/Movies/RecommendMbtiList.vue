<template>
    <div class="container">
        <h3 class="text-white mb-3 mt-3">{{ userStore.user.mbti }}가 좋아하는 영화!</h3>
        <div class="d-flex">
            <RecommendMbtiCard
                v-for="movie in filteredMovieList"
                :key="movie.id"
                :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import RecommendMbtiCard from '@/components/Movies/RecommendMbtiCard.vue'
import { ref, onMounted, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMovieStore } from '@/stores/movie'

const movieStore = useMovieStore()
const userStore = useUserStore()

const mbtiKeywords = {
    ESFJ: ['배려', '관심', '감성'],
    ENFP: ['활동', '창의', '풍부'],
    ENFJ: ['감정'],
    ENTP: ['노력', '유쾌'],
    ENTJ: ['용기', '정치'],
    ESFP: ['당당', '자유'],
    ESTP: ['마술', '이목', '놀라운'],
    ESTJ: ['규칙', '상상력', '해리 포터'],
    INFP: ['조용', '상상력'],
    INFJ: ['신념', '실현', '정의'],
    INTP: ['독특', '호기심', '과학'],
    INTJ: ['전력', '계산', '가상'],
    ISFP: ['변화', '혁신', '예술'],
    ISFJ: ['따뜻', '감동', '마음씨'],
    ISTP: ['흥미', '도전'],
    ISTJ: ['혼자']
}

const filteredMovieList = computed(() => {
    const keywords = mbtiKeywords[userStore.user.mbti] || [];
    return movieStore.movies.filter(movie => 
        keywords.some(keyword => movie.overview.includes(keyword))
    )
})

// const movieList = ref([])
// for (let i = 0; i < movieStore.movies.length; i++) {
//     if (userStore.user.mbti === 'ESFJ'){
//         if (movieStore.movies[i].overview.includes('배려')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('관심')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('감성')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ENFP'){
//         if (movieStore.movies[i].overview.includes('활동')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('창의')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('풍부')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ENFJ'){
//         if (movieStore.movies[i].overview.includes('감정')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ENTP'){
//         if (movieStore.movies[i].overview.includes('노력')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('유쾌')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ENTJ'){
//         if (movieStore.movies[i].overview.includes('용기')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('정치')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ESFP'){
//         if (movieStore.movies[i].overview.includes('당당')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('자유')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ESTP'){
//         if (movieStore.movies[i].overview.includes('마술')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('이목')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('놀라운')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ESTJ'){
//         if (movieStore.movies[i].overview.includes('규칙')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('상상력')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].title.includes('해리 포터')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'INFP'){
//         if (movieStore.movies[i].overview.includes('조용')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('상상력')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'INFJ'){
//         if (movieStore.movies[i].overview.includes('신념')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('실현')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('정의')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'INTP'){
//         if (movieStore.movies[i].overview.includes('독특')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('호기심')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('과학')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'INTJ'){
//         if (movieStore.movies[i].overview.includes('전력')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('계산')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('가상')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ISFP'){
//         if (movieStore.movies[i].overview.includes('변화')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('혁신')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('예술')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ISFJ'){
//         if (movieStore.movies[i].overview.includes('따뜻')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('감동')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('마음씨')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ISTP'){
//         if (movieStore.movies[i].overview.includes('흥미')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//         if (movieStore.movies[i].overview.includes('도전')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
//     if (userStore.user.mbti === 'ISTJ'){
//         if (movieStore.movies[i].overview.includes('혼자')) {
//             if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
//             } else {
//                 movieList.value.push(movieStore.movies[i])
//             }
//         }
//     }
// }

</script>

<style scoped>

</style>