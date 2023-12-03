<template>
    <div class="card ms-3" @click="goArticle(article)">
        <h5 class="fw-bold">{{ article.title }}</h5>
        <p>{{ article.content }}</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

defineProps({
    article: Object
})

const goArticle = function (article) {
    router.push({ name: 'articleDetail', params: { id: `${article.id}`}})
}
</script>

<style scoped>
.card {
    transition: transform 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100px;
    height: 100px;
    text-align: center;
}

.card:hover {
    transform: scale(1.03);
}
</style>