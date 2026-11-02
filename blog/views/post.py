from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from ..serializers import PostSerializer
from ..serializers import UserSerializer
from ..models import Post





class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET'])
def get_posts(request):
    try:
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))
        start = (page - 1) * limit
        end = start + limit

        posts = Post.objects.all()[start:end]
        serializer = PostSerializer(posts, many=True)
        return Response(
            {'posts': serializer.data, 'page': page, 'limit': limit}
        )
    except Exception:
        return Response(
            {"error":"An unexpected error occured."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )