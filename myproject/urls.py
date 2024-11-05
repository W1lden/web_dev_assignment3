from django.contrib import admin
from django.urls import path, include
from blog.views import PostListView, PostDetailView, create_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
