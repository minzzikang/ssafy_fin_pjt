from django.urls import path
from . import views

urlpatterns = [
    path('getdatas/', views.getdatas),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>', views.movie_detail),
    path('movies/comment', views.comment_list),
    path('movies/comment/<int:comment_pk>', views.comment_detail),
    path('movies/<int:movie_pk>/comment', views.comment_create),
    path('movies/<int:movie_pk>/likes', views.likes),
]
