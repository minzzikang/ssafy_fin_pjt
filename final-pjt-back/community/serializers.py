from rest_framework import serializers
from .models import Article, Articlecomment


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Articlecomment
        fields = '__all__'
        read_only_fields = ('user', 'article',)


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comment_count = serializers.IntegerField(source='articlecomment_set.count', read_only=True)
    like_count = serializers.IntegerField(source='article_like_users.count', read_only=True)
    articlecomment_set = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    articlecomment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='articlecomment_set.count', read_only=True)
    like_count = serializers.IntegerField(source='article_like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'article_like_users', 'is_like',)