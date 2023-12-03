<template>
    <div class="d-flex p-4" v-if="movieStore.movie">
        <Navbar />
        <div class="d-flex flex-column">
            <img :src="`https://image.tmdb.org/t/p/w300${movieStore.movie.poster_path}`" alt="poster">
            <font-awesome-icon :icon="['fas', 'circle-chevron-left']"
                style="color: #f5f5f5;" size="2xl" class="back-icon"
                @click="goBack"/>
            <span>다른 영화</span>
        </div>
        <div class="d-flex flex-column ms-3">
            <div class="title-box">
                <h3>{{ movieStore.movie.title }}</h3>
                <div v-for="(genr, index) in movieStore.movie.genres" :key="index"
                :class="['badge', 'text-bg', genreClass(genr.name)]">
                    {{ genr.name }}
                </div>
                <div class="badge text-warning ms-2">전문가 평점 : {{ movieStore.movie.vote_average }}</div>
            </div>
            <div class="align-self-start">
                <YoutubeTrailerModal :movie="movieStore.movie" />
            </div>
            <div class="movie-infos">
                <p>{{ shortOverview }}</p>
                <h6>감독 : {{ movieStore.movie.director.name }}</h6>
                <div class="d-flex flex-column">
                    <span class="mb-2 mt-2">출연진</span>
                    <h6 v-for="(actor, index) in limitActors" :key="index">
                        {{ actor.name }}
                    </h6>
                    <span v-if="movieStore.movie.actors.length > 3">...</span>
                </div>
            </div>
            <div class="mb-2">
                <font-awesome-icon :icon="[checkLike ? 'fas' : 'far', 'heart']"
                    @click="addLike(movieStore.movie.id)" class="heart-icon"/>
                <span class="text-white ms-2">{{ movieStore.movie.like_count }}</span>
                <font-awesome-icon :icon="['fas', 'star']" style="color: #ffd500;" class="ms-3"/>
                <span class="ms-2">{{ averageRating }}</span>
            </div>
            <div class="community-card">
            <MovieReviewList :movie="movieStore.movie" @new-comment="handleNewComment" @delete-comment="handleDeleteComment"
                @update-comment="handleUpdateComment" />
            </div>
        </div>
    </div>
</template>

<script setup>
import YoutubeTrailerModal from '@/components/Movies/YoutubeTrailerModal.vue'
import MovieReviewList from '@/components/Movies/MovieReviewList.vue'
import Navbar from '@/components/Movies/Navbar.vue'
import { onMounted, ref, computed } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const route = useRoute()
const movieStore = useMovieStore()
const userStore = useUserStore()
const genreClass = (genreName) => genreName.toLowerCase().replace(/\s+/g, '-');

onMounted(() => {
    movieStore.getMovieDetail()
    userStore.getUser()
    const total = ref(0)
    // const ratings = movieStore.movie.moviecomment_set.forEach(item => {
    //     total.value += item.rating
    // })
})

const limitActors = computed(() => {
    return movieStore.movie.actors.slice(0, 3)
})

const shortOverview = computed(() => {
    return movieStore.movie.overview.length > 150
    ? movieStore.movie.overview.slice(0, 150) + '...중략'
    : movieStore.movie.overview
})

const addLike = function (movieId) {
    axios({
            method: 'post',
            url: `${movieStore.API_URL}/api/v1/movies/${route.params.id}/likes`,
            headers: {
                Authorization: `Token ${movieStore.token}`
            }
        })
            .then((res) => {
                movieStore.getMovieDetail()
            })
            .catch((err) => {
                console.error(err)
            })
}


const averageRating = computed(() => {
    const total = ref(0)
    const len = ref(0)
    movieStore.movie.moviecomment_set.forEach(item => {
        total.value += item.rating
        len.value += 1
    })
    if (total.value) {
        return (total.value / len.value).toFixed(2)
    } else {
        return '평점을 남겨주세요.'
    }

})

const checkLike = computed(() => {
    if (movieStore.movie.movie_like_users.includes(userStore.user.pk)) {
        return true
    } else {
        return false
    }
})

const handleNewComment = (newComment) => {
    movieStore.movie.moviecomment_set.push(newComment)
}

const handleDeleteComment = (commentId) => {
    const index = movieStore.movie.moviecomment_set.findIndex((comment) => comment.id === commentId)
    movieStore.movie.moviecomment_set.splice(index, 1)
}

const handleUpdateComment = (updatedComment) => {
    console.log(updatedComment)
    const index = movieStore.movie.moviecomment_set.findIndex((comment) => comment.id === updatedComment.id)
    movieStore.movie.moviecomment_set[index] = updatedComment
}

const goBack = function () {
    router.push({ name: 'recommend' })
}
</script>

<style scoped>
.heart-icon {
    color: red;
}
img {
    width: 300px;
    height: 500px;
    margin-left: 20px;
}
h3, p, h6, span {
    color: #f5f5f5;
}

h3 {
    margin-right: 10px;
}
.title-box {
    display: flex;
    align-items: center;
}

.movie-infos {
    width: 800px;
}

.back-icon {
    align-self: flex-start;
    margin: 10px 20px;
}
.역사 {
    background-color: burlywood;
}
.tv영화 {
    background-color: lightcyan;
}
.드라마 {
    background-color: #D3D3D3;
}
.가족 {
    background-color: #F5F5DC;
}
.다큐멘터리 {
    background-color: #C0C0C0;
}
.액션 {
    background-color: #0000FF;
}
.스릴러 {
    background-color: #FF0000;
}
.범죄 {
    background-color: #808080;
}
.모험 {
    background-color: #32CD32;
}
.애니메이션{
    background-color: #FFD700;
}
.음악 {
    background-color: #FFA500;
}
.로맨스 {
    background-color: #FFB6C1;
}
.코미디 {
    background-color: #4e8f4e;
}
.공포 {
    background-color: #8B0000;
}
.미스터리 {
    background-color: darkkhaki;
}
.전쟁 {
    background-color: #EB0000;
}
.서부 {
    background-color: #F4A460;
}
.판타지 {
    background-color: #800080;
}
.sf {
    background-color: #008B8B;
}
</style>