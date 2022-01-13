from rest_framework import generics
from rest_framework import permissions
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly


class PostUserWritePermission(BasePermission):
    message='수정은 해당 글의 글쓴이만 할 수 있어요.'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=Post.postobjects.all()
    serializer_class =PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset= Post.objects.all()
    serializer_class = PostSerializer