from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from ..serializers import PostSerializer
from ..serializers import UserSerializer
from ..models import Post
from ..ai_content.service.summarize import PostNotFound, summarize_post




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


@api_view(["POST"])
def summarize_post_view(request, post_id):
    try:
        result = summarize_post(post_id)
    except PostNotFound as error:
        return Response({"error": str(error)}, status=status.HTTP_404_NOT_FOUND)
    except ValueError as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(result, status=status.HTTP_200_OK)