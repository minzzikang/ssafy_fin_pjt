<template>
    <div class="mb-3 mt-3">
        <div class="m-3">
            <h3 class="card-title fw-bold mb-3" @click="goDetail(article)">
                {{ article.title }}
            </h3>
            <div class="like-post">
                <font-awesome-icon :icon="['fas', 'heart']"/>
                <span class="ms-2">{{ article.like_count }}</span>
            </div>
            <div class="d-flex align-items-center">
                <p class="mt-3">{{ article.username }}</p>
            </div>
            <hr>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

defineProps({
    article: Object
})

const router = useRouter()

const goDetail = function (article) {
    // console.log(article)
    router.push({ name: 'articleDetail', params: { id: `${article.id}`}})
}

</script>

<style scoped>
hr {
    color: #ccc;
}
</style>