from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.post import summarize_post_view
from blog.views.gen import generate_post
from .views import PostViewSet, get_posts

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('posts/get_post/', get_posts, name='get_post'),
    path('posts/generate/', generate_post, name='generate_post'),
    path("posts/<int:post_id>/summarize/", summarize_post_view, name="summarize_post"),
    path("posts/<str:post_id>/summarize/", summarize_post_view, name="summarize_post"),
]
urlpatterns +=router.urls





