<template>
    <div class="d-flex justify-content-center">
        <div class="d-flex w-100 justify-content-center align-items-center">
            <form @submit.prevent="signUp" class="form-container w-50 bg-white p-4 border rounded">
                <h4>회원 가입을 환영합니다!</h4>
                <div class="mt-3">
                    <label for="username">아이디</label>
                    <input type="text" name="username" id="username" class="form-control mb-3" v-model.trim="username">
                    <label for="PW">비밀번호</label>
                    <input type="password" name="PW" id="PW" class="form-control mb-3" 
                        placeholder="영문, 숫자, 특문 중 2개 조합 8자 이상" v-model.trim="password1">
                    <label for="pwCheck">비밀번호 확인</label>
                    <input type="password" name="pwCheck" id="pwCheck" class="form-control mb-3" v-model.trim="password2">

                    <label for="nickname">닉네임</label>
                    <input type="text" name="nickname" id="nickname" class="form-control mb-3"
                        placeholder="2자 이상" v-model.trim="nickname">
                    
                    <label for="age">나이</label>
                    <input type="number" name="age" id="age" class="form-control mb-3" v-model.trim="age">

                    <label for="mbti">본인의 MBTI를 대문자로 입력해주세요! (선택사항)</label>
                    <input type="text" name="mbti" id="mbti" class="form-control mb-3" v-model.trim="mbti">
                    <input type="submit" class="btn btn-primary mt-3" value="가입하기">
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const nickname = ref('')
const age = ref('')
const mbti = ref('')

const signUp = function () {
    const payload = {
        username: username.value,
        password1: password1.value,
        password2: password2.value,
        nickname: nickname.value,
        mbti: mbti.value,
        age: age.value,
    }
    if (payload.mbti === 'ISTJ'
        || payload.mbti === 'ISFJ'
        || payload.mbti === 'INFJ'
        || payload.mbti === 'INTJ'
        || payload.mbti === 'ISTP'
        || payload.mbti === 'ISFP'
        || payload.mbti === 'INFP'
        || payload.mbti === 'INTP'
        || payload.mbti === 'ESTP'
        || payload.mbti === 'ESFP'
        || payload.mbti === 'ENFP'
        || payload.mbti === 'ENTP'
        || payload.mbti === 'ESTJ'
        || payload.mbti === 'ESFJ'
        || payload.mbti === 'ENFJ'
        || payload.mbti === 'ENTJ'
        || payload.mbti === ''
    ) {
        if (payload.mbti.includes('T')){
            alert('너 T야? ㅋㅋ')
        }
        store.signUp(payload)
    } else {
        alert('MBTI는 차라리 빈칸을 입력하세요...')
    }
}
</script>

<style scoped>

</style>