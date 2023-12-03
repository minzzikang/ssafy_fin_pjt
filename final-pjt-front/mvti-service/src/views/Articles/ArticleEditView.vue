<template>
    <div class="d-flex justify-content-center">
        <div class="d-flex w-100 justify-content-center align-items-center">
            <form @submit.prevent="updateArticle" class="form-container w-50 bg-white p-4 border rounded">
                <h3>글 수정하기</h3>
                <div class="mt-3">
                    <label for="title" class="form-label">제목:</label>
                    <input type="text" class="form-control mb-3" id="title" name="title" v-model.trim="title">

                    <label for="content" class="form-label">내용:</label>
                    <textarea class="form-control mb-3" id="content" name="content" rows="5" v-model.trim="content"></textarea>
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
import { useRoute, useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()
const route = useRoute()

const title = ref('')
const content = ref('')
const articleId = ref(route.params.id)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/community/article/${articleId.value}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    }).then(res => {
        const article = res.data
        title.value = article.title
        content.value = article.content
    })
})

const updateArticle = function () {
    axios({
        method: 'put',
        url: `${store.API_URL}/community/article/${articleId.value}`,
        data: {
            title: title.value,
            content: content.value,
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    }).then(res => {
        alert('글이 수정되었습니다.')
        router.push({ name: 'articleDetail'})
    }).catch(err => {
        console.log(err)
    })
}
</script>

<style scoped>

</style>