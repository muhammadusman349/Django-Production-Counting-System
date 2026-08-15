from django.urls import path

from .views import (
    ArticleApiView,
    ArticleSizeApiView,
    ArticleImageApiView,
)


urlpatterns = [

    # Article
    path("articles/",ArticleApiView.as_view(),name="article-list-create"),
    path("articles/<int:id>/",ArticleApiView.as_view(),name="article-detail"),

    # Article Size
    path("sizes/",ArticleSizeApiView.as_view(),name="article-size-list-create"),
    path("sizes/<int:id>/",ArticleSizeApiView.as_view(),name="article-size-detail"),
]