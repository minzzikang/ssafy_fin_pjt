import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
	const router = useRouter()
	const movies = ref([])
	const API_URL = 'http://127.0.0.1:8000'

	const token = ref(null)

	const isLogin = computed(() => {
		if (token.value === null) {
			return false
		} else {
			return true
		}
	})
	
	const getMovies = function () {
		axios({
			method: 'get',
			url: `${API_URL}/api/v1/movies/`,
			headers: {
				Authorization: `Token ${token.value}`
			}
		}).then((res) => {
			movies.value = res.data
		}).catch((err) => {
			console.log(err)
		})
	}

	const route = useRoute()
	const movie = ref(null)
	const getMovieDetail = function () {
	  axios({
		method: 'get',
		url: `${API_URL}/api/v1/movies/${route.params.id}`,
		headers: {
		  Authorization: `Token ${token.value}`
	  }
	  })
		.then((res) => {
			movie.value = res.data
		})
		.catch((err) => {
			console.log(err)
		})
	  }

	const logIn = function (payload) {
		const { username, password } = payload

		axios({
			method: 'post',
			url: `${API_URL}/accounts/login/`,
			data: {
				username, password
			}
		}).then((res) => {
			// console.log(res.data)
			token.value = res.data.key
			router.push({ name: 'recommend' })
		}).catch((err) => {
			for (let i = 0; i < Object.values(err.response.data).length; i++) {
				for (let j = 0; j < Object.values(err.response.data)[i].length; j++) {
					alert(Object.values(err.response.data)[i][j])
				}
			}
		})
	}

	const logOut = function () {
		axios({
			method: 'post',
			url: `${API_URL}/accounts/logout/`,
		}).then(res => {
			alert('다음에 또 봐요~!')
			router.push({ name: 'home' })
		}).catch(err => {
			console.log(err)
		})
	}

	const signUp = function (payload) {
		const { username, password1, password2, nickname, mbti, age } = payload

		axios({
			method: 'post',
			url: `${API_URL}/accounts/signup/`,
			data: {
				username, password1, password2, nickname, mbti, age
			}
		}).then((res) => {
			const password = password1
			if (mbti.includes('T')) {
				alert('죄송함당 ㅎㅎ 회원이 되신 걸 환영합니다!')
			} else {
				alert('F시네용ㅎㅎ 회원이 되신 걸 환영합니다!')
			}
			if (age <= 10 || age >= 100) {
				alert(`${payload.age}살 맞죵? ㅎㅎ; 거짓말이라면 회원정보에서 수정 부탁드립니다 ㅎㅎ`)
			}
			logIn({ username, password })
		}).catch((err) => {
			for (let i = 0; i < Object.values(err.response.data).length; i++) {
				for (let j = 0; j < Object.values(err.response.data)[i].length; j++) {
					if (Object.values(err.response.data)[i][j] === '유효한 정수(integer)를 넣어주세요.') {
						alert('나이는 웬만하면 입력해 주시죵 ^^7~')
					} else if (Object.values(err.response.data)[i][j] === 'User의 username은/는 이미 존재합니다.') {
						alert('하핫 이미 있는 아이디네용;')
					} else if (Object.values(err.response.data)[i][j] === '비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.') {
						alert('비밀번호 8자 이상 하라니까용;')
					} else if (Object.values(err.response.data)[i][j] === '비밀번호가 너무 일상적인 단어입니다.') {
						alert('비밀번호 이렇게 쉬우면 금방 뚫려용;')
					} else if (Object.values(err.response.data)[i][j] === '두 개의 패스워드 필드가 서로 맞지 않습니다.') {
						alert('비밀번호가 틀리다네용;')
					} else if (Object.values(err.response.data)[i][j] === '이 필드는 blank일 수 없습니다.') {
						alert('비밀번호는 입력하셔야죵;')
					} else {
						alert(Object.values(err.response.data)[i][j])
					}
				}
			}
			
		})
	}

	return { movies, token, API_URL, isLogin, getMovies, signUp, logIn, logOut, getMovieDetail, movie }
}, { persist: true })
