from rest_framework.generics import CreateAPIView
from ..serializers import CommentSerializer


class CreateCommentView(CreateAPIView):
    serializer_class = CommentSerializer