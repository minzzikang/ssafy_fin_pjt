<template>
    <div class="container" v-if="store.article">
        <div class="d-flex flex-cloumn card">
            <div class="title-top">
                <h2>{{ store.article.title }}</h2>
                <font-awesome-icon :icon="['fas', 'circle-chevron-left']" size="2xl" class="back-icon" @click="goBack" />
            </div>
            <p>{{ store.article.username }}</p>
            <h5>{{ store.article.content }}</h5>
            <div class="d-flex align-items-center justify-content-between">
                <div>
                    <font-awesome-icon :icon="[checkLike ? 'fas' : 'far', 'heart']"
                        @click="addLike(store.article.id)"/>
                        <span class="ms-2">{{ store.article.like_count }}</span>
                    <font-awesome-icon :icon="['fas', 'comment']" class="ms-3"/>
                    <span class="ms-2">{{ store.article.comment_count }}</span>
                </div>
                <div class="dates">
                    <p class="mb-0">작성일: {{ formatDate(store.article.created_at) }}</p>
                    <p>수정일: {{ formatDate(store.article.updated_at) }}</p>
                </div>
            </div>
            <CommentList :article="store.article" @new-comment="handleNewComment" @delete-comment="handleDeleteComment"
                @update-comment="handleUpdateComment" />
            <div class="d-flex align-items-center justify-content-end">
                <font-awesome-icon :icon="['fas', 'pen']" class="ms-2" @click="goEdit" v-if="store.article.user === userStore.user.pk"/>
                <font-awesome-icon :icon="['fas', 'trash-can']" class="ms-3"
                    @click="store.deleteArticle(store.article.id)" v-if="store.article.user === userStore.user.pk"/>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
import CommentList from '@/components/Articles/CommentList.vue'

const route = useRoute()
const router = useRouter()
const store = useArticleStore()
const movieStore = useMovieStore()
const userStore = useUserStore()

onMounted(() => {
    store.getArticleDetail()
    userStore.getUser()
})

const formatDate = function (dateTime) {
  return moment(dateTime).format('YYYY-MM-DD HH:mm:ss')
}

const addLike = function (articleId) {
    axios({
            method: 'post',
            url: `${store.API_URL}/community/article/${route.params.id}/likes`,
            headers: {
                Authorization: `Token ${movieStore.token}`
            }
        })
            .then((res) => {
                store.getArticleDetail()
            })
            .catch((err) => {
                console.error(err)
            })
}

const checkLike = computed(() => {
    if (store.article.article_like_users.includes(userStore.user.pk)) {
        return true
    } else {
        return false
    }
})

const handleNewComment = (newComment) => {
    store.article.articlecomment_set.push(newComment)
    store.article.comment_count += 1
}

const handleDeleteComment = (commentId) => {
    const index = store.article.articlecomment_set.findIndex((comment) => comment.id === commentId)
    store.article.articlecomment_set.splice(index, 1)
    store.article.comment_count -= 1
}

const handleUpdateComment = (updatedComment) => {
    const index = store.article.articlecomment_set.findIndex((comment) => comment.id === updatedComment.id)
    store.article.articlecomment_set[index] = updatedComment
}

const goBack = function () {
    router.push({ name: 'article' })
}

const goEdit = function () {
    router.push({ name: 'articleEdit' })
}

</script>

<style scoped>
.container {
    max-width: 700px;
    padding: 20px;
    margin: auto;
}

.card {
    background-color: #f9f9f9;
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 20px;
}

.card h3 {
    color: #333;
    font-size: 24px;
}

.title-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.dates {
    align-self: flex-end;
    text-align: right;
    font-size: 0.8rem;
    color: #666;
}
</style>