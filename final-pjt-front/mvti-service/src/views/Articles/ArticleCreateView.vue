<template>
    <div class="d-flex justify-content-center">
        <div class="d-flex w-100 justify-content-center align-items-center">
            <form @submit.prevent="store.createArticle" class="form-container w-50 bg-white p-4 border rounded">
                <h3>새 글쓰기</h3>
                <div class="mt-3">
                    <label for="title" class="form-label">제목</label>
                    <input type="text" class="form-control mb-3" id="title" name="title" v-model.trim="store.title">

                    <label for="content" class="form-label">내용</label>
                    <textarea class="form-control mb-3" id="content" name="content" rows="5" v-model.trim="store.content"></textarea>
                    <div class="d-grid mt-3">
                        <input type="submit" class="btn btn-primary" value="작성 완료">
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()

</script>

<style scoped>

</style>