from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

class ArticleApiView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if "id" in self.kwargs:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
            return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
            return super().put(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
            return super().patch(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)