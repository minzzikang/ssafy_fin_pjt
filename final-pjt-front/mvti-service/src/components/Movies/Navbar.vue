<template>
    <div class="d-flex">
        <div class="nav-bar d-flex flex-column">
            <font-awesome-icon :icon="['fas', 'magnifying-glass']" style="color: #f5f5f5;" size="2xl"
                @click="goSearch" />
            <font-awesome-icon :icon="['fas', 'people-group']" style="color: #f5f5f5;" size="2xl"
                @click="goCommunity" />
            <font-awesome-icon :icon="['fas', 'house']" style="color: #f5f5f5;" size="2xl" 
                @click="goHome" />
            <font-awesome-icon :icon="['fas', 'user-gear']" style="color: #f5f5f5;" size="2xl"
                @click="goUser" />
            <font-awesome-icon :icon="['fas', 'arrow-right-from-bracket']" 
                size="2xl" style="color: #f5f5f5;"
                @click="store.logOut"/>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const router = useRouter()
const store = useMovieStore()

const goSearch = function () {
    router.push({ name: 'search' })
}

const goCommunity = function () {
    router.push({ name: 'article' })
}

const goHome = function () {
    router.push({ name: 'recommend' })
}

const goUser = function () {
    router.push({ name: 'user'})
}
</script>

<style scoped>
.nav-bar {
    background-color: rgba(73, 73, 73, 0.308);
    border: 1px solid #f5f5f5;
    border-radius: 10px;
    position: sticky;
    top: 0;
    z-index: 1000;
    width: 50px;
    height: 50%;
    margin: 20px auto;
    padding: 10px;
    align-items: center;
    justify-content: space-evenly;
}
</style>