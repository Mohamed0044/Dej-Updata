"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog.views.post import CreateUserView, PostViewSet
from blog.views.cat import CreateCategoryView
from blog.views.com import CreateCommentView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('api/users/', CreateUserView.as_view(), name='create_user'),
    path('api/categories/', CreateCategoryView.as_view(), name='create_category'),
    path('api/comments/', CreateCommentView.as_view(), name='create_comment'),
    path('api/posts/', PostViewSet.as_view({'post': 'create'}), name='create_post'),
]
    


