from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import requests, json
from django.conf import settings
from .models import Movie, Moviecomment
from .serializers import MovieSerializer, MovieDetailSerializer, CommentSerializer, GenreSerializer

# Create your views here.
TMDB_URL = 'https://api.themoviedb.org/3/'
TMDB_API_KEY = settings.TMDB_API_KEY

# api_key로 데이터 받아오기
@api_view(['GET'])
def getdatas(request):

    # 전체 데이터
    total_list = []
    
    # 장르 받아오기
    genre_url = f"{TMDB_URL}genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(genre_url).json()
    for genre in genres['genres']:
        fields = {
            'name':genre['name']
        }

        genre = {
            'model': 'movies.Genre',
            'pk': genre['id'],
            'fields': fields
        }
        total_list.append(genre)


    # 영화데이터 받아오기
    # for i in range(1, 300):
    for i in range(1, 200):
        movie_url = f"{TMDB_URL}movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(movie_url).json()

        for movie in movies['results']:
            if movie.get('release_date', '') and (movie.get('overview') != '' and movie.get('poster_path') != None and movie.get('release_date') != None):
                # 영화 상세 정보
                movie_detail_url = f"{TMDB_URL}movie/{movie['id']}?api_key={TMDB_API_KEY}&language=ko-KR"
                movie_detail = requests.get(movie_detail_url).json()
                # 배우, 감독 정보
                movie_people_url = f"{TMDB_URL}movie/{movie['id']}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                movie_people = requests.get(movie_people_url).json()
                # 예고편 정보
                movie_trailer_url = f"{TMDB_URL}movie/{movie['id']}/videos?api_key={TMDB_API_KEY}&language=ko-KR"
                movie_trailer = requests.get(movie_trailer_url).json()
                # print(movie_trailer)

                actors = []
                actor_list = []
                if len(movie_people['cast']) < 7:
                    for i in range(len(movie_people['cast'])):
                        actors.append(movie_people['cast'][i]['id'])
                        actor_list.append(movie_people['cast'][i])
                else:
                    for i in range(7):
                        actors.append(movie_people['cast'][i]['id'])
                        actor_list.append(movie_people['cast'][i])

                director = ''
                director_list = []
                for direct in movie_people['crew']:
                    if direct['department'] == 'Directing':
                        director = direct['id']
                        director_list.append(direct)
                        break
                print(director)

                # 영화에 출연한 배우 받아오기
                for actor in actor_list:
                    fields = {
                        'name':actor['name']
                    }
                    actor = {
                        'model': 'movies.Actor',
                        'pk': actor['id'],
                        'fields': fields
                    }
                    total_list.append(actor)

                # 영화 만든 감독 받아오기
                if director_list:
                    fields = {
                        'name':director_list[0]['name']
                    }
                    directors = {
                        'model': 'movies.Director',
                        'pk': director_list[0]['id'],
                        'fields': fields
                    }
                    total_list.append(directors)

                # 영화 정보 받아오기
                if director_list and movie_trailer['results']:
                    fields = {
                        'actors': actors,
                        'adult': movie['adult'],
                        'director': director,
                        'genres': movie['genre_ids'],
                        'overview': movie['overview'],
                        'popularity': movie['popularity'],
                        'poster_path': movie['poster_path'],
                        'release_date': movie['release_date'],
                        'runtime': movie_detail['runtime'],
                        'trailer_key': movie_trailer['results'][0]['key'],
                        'title': movie['title'],
                        'vote_average': movie['vote_average'],
                        'vote_count': movie['vote_count'],
                        'movie_like_users': []
                    }
                    movie = {
                        'model': 'movies.Movie',
                        'pk': movie['id'],
                        'fields': fields
                    }
                    total_list.append(movie)

    #             movie_list.append(movie)
    #             serializer = MovieSerializer(data=movie)
    #             if serializer.is_valid(raise_exception=True):
    #                 serializer.save()
    # return Response(serializer.data)

    with open("movies/fixtures/datas.json", "w", encoding="utf-8") as w:
        json.dump(total_list, w, indent=4, ensure_ascii=False)

    return Response(total_list)



# 전체 movie 정보 받아오기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 영화 상세정보 받아오기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


# 영화 전체 댓글 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_list(request):
    comments = Moviecomment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 영화 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 영화 상세정보에서 댓글 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Moviecomment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 영화 좋아요(찜목록)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.movie_like_users.filter(pk=request.user.pk).exists():
        movie.movie_like_users.remove(request.user)
    else:
        movie.movie_like_users.add(request.user)
    return Response(status=status.HTTP_200_OK)
