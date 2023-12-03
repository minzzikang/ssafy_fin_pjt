<template>
    <div class="d-flex justify-content-center">
        <div class="d-flex w-100 justify-content-center align-items-center">
            <form @submit.prevent="updateUser" class="form-container w-50 bg-white p-4 border rounded">
                <h3>회원정보 수정</h3>
                <div class="mt-3">
                    <label for="nickname" class="form-label">닉네임:</label>
                    <input type="text" class="form-control mb-3" id="nickname" name="nickname" v-model.trim="nickname">

                    <label for="mbti" class="form-label">MBTI(대문자로 입력해 주세요!):</label>
                    <input type="text" class="form-control mb-3" id="mbti" name="mbti" v-model.trim="mbti">

                    <label for="age" class="form-label">나이:</label>
                    <input type="number" class="form-control mb-3" id="age" name="age" v-model.trim="age">

                    <div class="d-grid mt-3">
                        <input type="submit" class="btn btn-primary" value="수정 완료">
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'

const movieStore = useMovieStore()
const userStore = useUserStore()
const router = useRouter()
const route = useRoute()

const nickname = ref('')
const mbti = ref('')
const age = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${movieStore.API_URL}/accounts/user`,
        headers: {
            Authorization: `Token ${movieStore.token}`
        }
    }).then(res => {
        console.log(res.data)
        const user = res.data
        nickname.value = user.nickname
        mbti.value = user.mbti
        age.value = user.age
    })
})

const updateUser = function () {
    if ((mbti.value === 'ISTJ'
        || mbti.value === 'ISFJ'
        || mbti.value === 'INFJ'
        || mbti.value === 'INTJ'
        || mbti.value === 'ISTP'
        || mbti.value === 'ISFP'
        || mbti.value === 'INFP'
        || mbti.value === 'INTP'
        || mbti.value === 'ESTP'
        || mbti.value === 'ESFP'
        || mbti.value === 'ENFP'
        || mbti.value === 'ENTP'
        || mbti.value === 'ESTJ'
        || mbti.value === 'ESFJ'
        || mbti.value === 'ENFJ'
        || mbti.value === 'ENTJ'
        || mbti.value === '')
    ){
        axios({
        method: 'put',
        url: `${movieStore.API_URL}/accounts/userupdate/${userStore.user.pk}`,
        data: {
            nickname: nickname.value,
            mbti: mbti.value,
            age: age.value,
        },
        headers: {
            Authorization: `Token ${movieStore.token}`
        }
        }).then(res => {
            if (age.value < 10) {
                alert(`${age.value}살이요? 정말 어리시네용 믿습니다 ㅎㅎ`)
            } else if (age.value > 100) {
                alert(`${age.value}세시라구요? 저희 서비스를 잘 즐겨주시기 바랍니다.`)
            } else {
                alert('회원 정보 수정 완-')
            }
            router.push({ name: 'user'})
        }).catch(err => {
            console.log(err.response.data.age[0])
            if (err.response.data.age[0] === '유효한 정수(integer)를 넣어주세요.') {
                alert('웬만하면 나이는 입력해 주시는게...')
            }
        })
    } else {
        alert('MBTI 입력 안하실거면 빈칸으로 두는게...')
    }
}
</script>

<style  scoped>

</style>