from django.db import models

# Create your models here.

class Article(models.Model):
    article_code = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ArticleSize(models.Model):
    article = models.ForeignKey(Article,on_delete=models.PROTECT,related_name="sizes")
    size = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["article", "size"],name="unique_article_size")]

    def __str__(self):
        return f"{self.article.name} - Size {self.size}"


class ArticleImage(models.Model):
    article = models.ForeignKey(Article,on_delete=models.PROTECT,related_name="images")
    image = models.ImageField(upload_to="article_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.article.name}"


#for future use, if we want to add videos to articles, we can uncomment the following code

# class ArticleVideo(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='videos')
#     video = models.FileField(upload_to='article_videos/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Video for {self.article.name}"