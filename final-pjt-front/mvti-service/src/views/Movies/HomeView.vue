<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()
const username = ref('')
const password = ref('')

const logIn = function () {
    const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<template>
    <div class="background d-flex flex-column">
        <div class="overlay">
            <div class="d-flex justify-content-center align-items-center mt-5">
                <img src="@/assets/mvti_logo.png" alt="logo">
            </div>
            <div class="container d-flex justify-content-center align-items-center flex-column w-100 mt-3">
                <div class="card w-25 p-2">
                    <form @submit.prevent="logIn" class="card-body">
                        <input class="form-control mb-2" type="text" placeholder="아이디를 입력하세요."
                            v-model.trim="username">
                        <input class="form-control mb-2" type="password" placeholder="비밀번호를 입력하세요."
                            v-model.trim="password">
                        <div class="d-flex justify-content-between">
                            <RouterLink :to="{ name: 'signup'}">회원이 아니신가요?</RouterLink>
                            <input type="submit" value="로그인" class="btn btn-primary btn-sm">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    
</template>

<style scoped>
.background {
  background-image: url('@/assets/background-img.png');
  overflow: hidden;
  background-size: contain;
  background-position: center;
}
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5); /* 오버레이 색상 및 투명도 */
}
.card {
    background-color: rgba(255, 255, 255, 0.8);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

img {
    width: 200px;
}
</style>