from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView


app_name = "blog"
urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("topic/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", BlogCreateView.as_view(), name="new")
]