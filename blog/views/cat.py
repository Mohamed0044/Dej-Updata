from rest_framework.generics import CreateAPIView
from ..serializers import CategorySerializer


class CreateCategoryView(CreateAPIView):
    serializer_class = CategorySerializer