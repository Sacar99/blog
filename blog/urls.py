from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = "blog"
urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("topic/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", BlogCreateView.as_view(), name="new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name='post_edit'),
    path("post/<int:pk>/del/", BlogDeleteView.as_view(), name="del"),
]