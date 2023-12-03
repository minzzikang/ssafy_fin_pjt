<template>
    <div class="card">
        <form @submit.prevent="createComment" class="d-flex">
            <div class="input-group">
                <input type="number" class="form-control" v-model.number="rating"
                    min="0" max="10" placeholder="평점 (0~10)">
                <input type="text" class="form-control" v-model.trim="content"
                    placeholder="한 줄 리뷰 남기기">
                <input type="submit" value="등록" class="btn btn-dark">
            </div>
        </form>
        <p v-for="comment in movie.moviecomment_set"
            :key="comment.id"
            :comment="comment">
            <div v-if="isEditing[comment.id]" class="comment-group">
                <input type="number" v-model="editingContent[comment.id].rating" class="form-control" />
                <input type="text" v-model="editingContent[comment.id].content" class="form-control" />
                <font-awesome-icon :icon="['fas', 'circle-check']" size='xl' class="ms-3"
                    @click="saveEdit(comment.id)"/>
                <font-awesome-icon :icon="['fas', 'circle-xmark']" size='xl' class="ms-2"
                    @click="cancelEdit(comment.id)"/>
            </div>
                <span>{{ comment.username }}</span>
                <span class="rating fw-bold ms-3">{{ comment.rating }}점</span>
                <span class="ms-4">{{ comment.content }}</span>
                <font-awesome-icon :icon="['fas', 'pen']" style="color: #aaaaaa;" class="ms-4" 
                    @click="startEdit(comment)"
                    v-if="comment.user === userStore.user.pk"/>
                <font-awesome-icon :icon="['fas', 'trash-can']" style="color: #aaaaaa;" class="ms-3"
                    @click="deleteComment(comment.id)"
                    v-if="comment.user === userStore.user.pk"/>
            <hr>
        </p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
const route = useRoute()
const movieStore = useMovieStore()
const rating = ref(null)
const content = ref('')
const emit = defineEmits(['newComment', 'deleteComment', 'updateComment'])
const userStore = useUserStore()

const props = defineProps({
    movie: Object
})

const movieId = ref(route.params.id)
const isEditing = ref({})
const editingContent = ref({})

const startEdit = (comment) => {
    isEditing.value[comment.id] = true
    editingContent.value[comment.id] = {content: comment.content, rating: comment.rating}
    console.log(editingContent.value)
}

const saveEdit = (commentId) => {
    updateComment(commentId, editingContent.value[commentId])
    isEditing.value[commentId] = false
}

const cancelEdit = (commentId) => {
    isEditing.value[commentId] = false
}

const createComment = function () {
    axios({
        method: 'post',
        url: `${movieStore.API_URL}/api/v1/movies/${movieId.value}/comment`,
        data: {
            movie: route.params.id,
            rating : rating.value,
            content: content.value
        },
        headers: {
            Authorization: `Token ${movieStore.token}`
        },
    }).then(res => {
        emit('newComment', res.data)
        content.value = ''
        rating.value = ''
    }).catch(err => {
        console.log(err)
    })
}

const updateComment = function (commentId, newContent) {
    axios({
        method: 'put',
        url: `${movieStore.API_URL}/api/v1/movies/comment/${commentId}`,
        data: {
            content: newContent.content,
            rating: newContent.rating
        },
        headers: {
            Authorization: `Token ${movieStore.token}`
        }
    }).then(res => {
        emit('updateComment', res.data)
    }).catch(err => {
        console.log(err)
    })
}

const deleteComment = function (commentId) {
    axios({
        method: 'delete',
        url: `${movieStore.API_URL}/api/v1/movies/comment/${commentId}`,
        headers: {
            Authorization: `Token ${movieStore.token}`
        }
    }).then(res => {
        emit('deleteComment', commentId)
    }).catch(err => {
        console.log(err)
    })
}

</script>

<style scoped>
.card {
    max-height: 250px;
    max-width: 750px;
    overflow: auto;
    padding: 10px;
    position: relative;
}

.input-group, .comment-group {
    display: flex;
    margin-bottom: 10px;
    align-items: center;
}

h6 {
    color: #f5f5f5;
}

.rating {
    background-color: rgba(255, 255, 0, 0.47);
    border-radius: 5px;
    width: 20px;
}
.btn {
    white-space: nowrap;
}

</style>