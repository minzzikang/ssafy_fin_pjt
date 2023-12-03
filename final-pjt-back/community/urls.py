from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list),
    path('article/<int:article_pk>', views.article_detail),
    path('comment/', views.comment_list),
    path('comment/<int:comment_pk>', views.comment_detail),
    path('article/<int:article_pk>/comment', views.comment_create),
    path('article/<int:article_pk>/likes', views.likes)
]
