from rest_framework import serializers

from .models import Article, ArticleSize, ArticleImage


class ArticleSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleSize
        fields = [
            "id",
            "size",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


class ArticleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleImage
        fields = [
            "id",
            "image",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


class ArticleSerializer(serializers.ModelSerializer):

    sizes = ArticleSizeSerializer(
        many=True,
        read_only=True
    )

    images = ArticleImageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Article

        fields = [
            "id",
            "article_code",
            "name",
            "description",
            "is_active",
            "sizes",
            "images",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "sizes",
            "images",
            "created_at",
            "updated_at",
        ]