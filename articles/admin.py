from django.contrib import admin

from .models import Article, ArticleSize, ArticleImage


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "article_code",
        "name",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "article_code",
        "name",
    )

    ordering = (
        "-created_at",
    )


@admin.register(ArticleSize)
class ArticleSizeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "article",
        "size",
        "created_at",
    )

    list_filter = (
        "size",
    )

    search_fields = (
        "article__article_code",
        "article__name",
        "size",
    )


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "article",
        "created_at",
    )

    search_fields = (
        "article__article_code",
        "article__name",
    )