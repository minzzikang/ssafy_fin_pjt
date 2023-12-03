<template>
    <div class="d-flex flex-column">
        <p class="mt-3">댓글 쓴 게시글</p>
        <div class="d-flex article-card">
            <UserCommentArticleCard 
                v-for="article in userCommentArticle"
                :key="article.id"
                :article="article"/>
        </div>
    </div>
</template>

<script setup>
import UserCommentArticleCard from '@/components/Users/UserCommentArticleCard.vue'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'

const articleStore = useArticleStore()
const userStore = useUserStore()

const userCommentArticle = computed(() => {
    return articleStore.articles.filter(article => {
        return article.articlecomment_set.some(comment => comment.username === userStore.user.username)
    })
})
// console.log(articleStore.articles)
</script>

<style scoped>
.article-card {
    margin: 0px;
}
</style>