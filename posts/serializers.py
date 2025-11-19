from rest_framework import serializers
from posts.models import Post, Like

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'text_twitter', 'image_twitter', 'created_at', 'likes_count']
        read_only_fields = ['author', 'created_at', 'likes_count']

        def get_likes_count(self, obj):
            return obj.likes.count()

class LikeSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'user', 'user_username', 'post', 'created_at']
        read_only_fields = ['user', 'created_at']