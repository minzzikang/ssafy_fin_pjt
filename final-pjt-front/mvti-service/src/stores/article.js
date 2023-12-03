import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { useMovieStore } from './movie'

export const useArticleStore = defineStore('article', () => {
    const router = useRouter()
    const route = useRoute()

    const articles = ref([])
    const article = ref(null)
    const API_URL = 'http://127.0.0.1:8000'

    const movieStore = useMovieStore()

    const getArticles = function () {
        axios({
            method: 'get',
            url: `${API_URL}/community/article/`,
            headers: {
                Authorization: `Token ${movieStore.token}`
            }
        })
            .then((res) => {
                articles.value = res.data
            })
            .catch((err) => {
                console.log(err)
            })
    }

    const getArticleDetail = function () {
        axios({
            method: 'get',
            url: `${API_URL}/community/article/${route.params.id}`,
            headers: {
                Authorization: `Token ${movieStore.token}`
            }
        })
            .then((res) => {
                article.value = res.data
            })
            .catch((err) => {
                console.error(err)
            })
    }

    const deleteArticle = function (articleId) {
        axios({
            method: 'delete',
            url: `${API_URL}/community/article/${articleId}`,
            headers: {
                Authorization: `Token ${movieStore.token}`
            }
        }).then(() => {
            router.push({ name: 'article' })
        }).catch(err => {
            console.log(err)
        })
    }

    const title = ref('')
    const content = ref('')

    const createArticle = function () {
        axios({
            method: 'post',
            url: `${API_URL}/community/article/`,
            data: {
                title: title.value,
                content: content.value,
            },
            headers: {
                Authorization: `Token ${movieStore.token}`
            }
        }).then(res => {
            // console.log(res)
            router.push({ name: 'article' })
        }).catch(err => {
            console.log(err)
        })
    }

    return {
        article, articles, API_URL, getArticles, movieStore, getArticleDetail,
        deleteArticle, title, content, createArticle,
    }
}, { persist: true })
