<template>
    <div class="d-flex">
        <Navbar />
        <div class="ms-4 mt-3 d-flex flex-column" style="color: #f5f5f5;">
            <div class="d-flex align-items-center mb-3">
                <h3 class="me-3">{{ user.username }} 님의 프로필</h3>
                <button class="btn2 btn btn-secondary btn-sm" @click="UserInfoUpdate">정보수정</button>
                <button class="btn btn-danger btn-sm" @click="signout">회원탈퇴</button>
                <font-awesome-icon :icon="['fas', 'key']" size="xl" style="color: #f5f5f5;"
                    class="icon ms-3 mt-2" @click="goUserUpdate"/>
            </div>
                
            <div class="d-flex flex-column">
                <UserLikeList />
                <hr>
            </div>
            <div class="d-flex flex-column">           
                <UserCommentMovieList />
                <hr>
            </div>
            <div class="d-flex flex-column"> 
                <UserArticleList />
                <hr>
            </div>
            <div class="d-flex flex-column"> 
                <UserCommentArticleList />
            </div>
        </div>
    </div>
</template>


<script setup>
import UserLikeList from '@/components/Users/UserLikeList.vue'
import UserCommentMovieList from '@/components/Users/UserCommentMovieList.vue'
import UserArticleList from '@/components/Users/UserArticleList.vue'
import UserCommentArticleList from '@/components/Users/UserCommentArticleList.vue'
import Navbar from '@/components/Movies/Navbar.vue'

import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useMovieStore()
const user = ref([])

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/accounts/user`,
        headers: {
        Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
        user.value = res.data
    })
    .catch((err) => console.log(err))
})

const signout = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/accounts/signout/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
    })
    .then((res) => {
        alert('다음에 또 방문해주세용 ㅠㅠ')
        store.token = null
        store.user = null
        router.replace({ name: 'home' })
    })
    .catch(err => console.log(err))
}

const goUserUpdate = function () {
    router.push({ name: 'userUpdate' })
}

const UserInfoUpdate = function () {
    router.push({ name: 'userInfoUpdate' })
}

</script>

<style scoped>
.ms-4.mt-3 {
    margin-left: 1.5rem;
    margin-top: 1rem;
    color: #f5f5f5;
}

h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.icon {
    align-self: flex-start;
    cursor: pointer;
    margin-right: 0.5rem;
}

/* 버튼 스타일 */
.btn {
    padding: 0.5rem 1rem;
    cursor: pointer;
    transition: background-color 0.2s;
}

.btn:hover {
    background-color: #911b00;
}

.btn2 {
    padding: 0.5rem 1rem;
    cursor: pointer;
    transition: background-color 0.2s;
}

.btn2:hover {
    background-color: darkslategray;
}
</style>