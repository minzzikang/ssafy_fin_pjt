<template>
    <div>
        <div class="container p-2">
            <ArticleCard 
            v-for="article in store.articles" :key="article.id"
            :article="article"
            />
        </div>
    </div>
</template>

<script setup>
import ArticleCard from '@/components/Articles/ArticleCard.vue'
import axios from 'axios'
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'

const store = useArticleStore()
const userStore = useUserStore()

onMounted(() => {
    store.getArticles()
    userStore.getUser()
})

</script>

<style scoped>
.container {
    background-color: white;
}
</style>