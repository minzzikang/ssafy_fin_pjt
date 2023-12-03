<template>
    <div class="d-flex flex-column">
        <p>좋아요한 게시글</p>
        <div class="article-card d-flex">
            <UserArticleCard
            v-for="article in userLikeArticle"
            :key="article.id"
            :article="article"/>
        </div>
    </div>
</template>

<script setup>
import UserArticleCard from '@/components/Users/UserArticleCard.vue'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'

const articleStore = useArticleStore()
const userStore = useUserStore()

const userLikeArticle = computed(() => {
    return articleStore.articles.filter(article => {
        return article.article_like_users.includes(userStore.user.pk);
    })
})

</script>

<style scoped>
.article-card {
    margin: 0px;
}
</style>