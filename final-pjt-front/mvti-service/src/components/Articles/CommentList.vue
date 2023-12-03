<template>
    <div>
        <form @submit.prevent="createComment" class="comment-form mb-3">
            <div class="input-group">
                <input type="text" id="comment" name="comment" v-model="content" placeholder="댓글을 입력하세요." class="form-control">
                <input type="submit" value="등록" class="btn btn-dark">
            </div>
        </form>
        <p v-for="comment in article.articlecomment_set"
            :key="comment.id"
            :comment="comment">
            <div v-if="isEditing[comment.id]" class="comment-group">
                <input type="text" v-model="editingContent[comment.id]" class="form-control" />
                <font-awesome-icon :icon="['fas', 'circle-check']" size='xl' class="ms-3"
                    @click="saveEdit(comment.id)"/>
                <font-awesome-icon :icon="['fas', 'circle-xmark']" size='xl' class="ms-2"
                    @click="cancelEdit(comment.id)"/>
            </div>
            <div v-else>
                <span class="fw-bold">{{ comment.username }}</span>
                <span class="ms-4">{{ comment.content }}</span>
                <font-awesome-icon :icon="['fas', 'pen']" style="color: #aaaaaa;" class="ms-4" 
                    @click="startEdit(comment)"
                    v-if="comment.user === userStore.user.pk"/>
                <font-awesome-icon :icon="['fas', 'trash-can']" style="color: #aaaaaa;" class="ms-3"
                    @click="deleteComment(comment.id)"
                    v-if="comment.user === userStore.user.pk"/>
            </div>
            <hr>
        </p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const store = useArticleStore()
const movieStore = useMovieStore()
const userStore = useUserStore()
const content = ref('')
const emit = defineEmits(['newComment', 'deleteComment', 'updateComment'])

const props = defineProps({
    article: Object
})


const checkComment = computed(() => {
    if (store.article.articlecomment_set.some(comment => comment.id === userStore.user.pk)) {
        return true
    } else {
        return false
    }
})

const articleId = ref(route.params.id)
const isEditing = ref({})
const editingContent = ref({})

const startEdit = (comment) => {
    isEditing.value[comment.id] = true
    editingContent.value[comment.id] = comment.content
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
        url: `${store.API_URL}/community/article/${articleId.value}/comment`,
        data: {
            article: route.params.id,
            content: content.value
        },
        headers: {
            Authorization: `Token ${movieStore.token}`
        },
    }).then(res => {
        emit('newComment', res.data)
        content.value = ''
    }).catch(err => {
        console.log(err)
    })
}

const updateComment = function (commentId, newContent) {
    axios({
        method: 'put',
        url: `${store.API_URL}/community/comment/${commentId}`,
        data: {
            content: newContent
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
        url: `${store.API_URL}/community/comment/${commentId}`,
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
.comment-form {
    display: flex;
    flex-direction: column;   
}

.input-group {
    display: flex;
}
.comment-group {
    display: flex;
    align-items: center;
}
</style>