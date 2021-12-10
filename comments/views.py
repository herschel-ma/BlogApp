from rest_framework import viewsets

from comments.models import Comment
from comments.serializers import CommentSerializer
from comments.permissions import IsAuthorOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [IsAuthorOrReadOnly]
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        serializer.save(isShow=True)
