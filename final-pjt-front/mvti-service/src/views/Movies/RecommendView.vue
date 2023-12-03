<template>
    <div class="d-flex">
        <Navbar />
        <div>
            <div v-if="userStore.user.mbti" class="mbti d-flex flex-column">
                <RecommendMbtiList class="ms-3" />
            </div>
            <div v-else class="d-flex flex-column">
                <NoMbti class="ms-3" />
            </div>
            <div class="today d-flex flex-column">
                <RecommendTodayList class="ms-3" />
            </div>
            <div class="age d-flex flex-column">
                <RecommendAgeList class="ms-3" />
            </div>
        </div>
    </div>
</template>

<script setup>
import RecommendTodayList from '@/components/Movies/RecommendTodayList.vue'
import RecommendMbtiList from '@/components/Movies/RecommendMbtiList.vue'
import RecommendAgeList from '@/components/Movies/RecommendAgeList.vue'
import NoMbti from '@/components/Movies/NoMbti.vue'
import Navbar from '@/components/Movies/Navbar.vue'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'

const movieStore = useMovieStore()
const userStore = useUserStore()

onMounted(() => {
    movieStore.getMovies()
    userStore.getUser()
})

</script>

<style scoped>
.nav-bar {
    position: sticky;
    top: 0;
}

.mbti, .today, .age {
    overflow-x: auto;
    white-space: nowrap;
}
</style>