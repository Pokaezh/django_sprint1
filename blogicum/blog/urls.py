from . import views

from django.urls import path

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("<slug:category_slug>/", views.category_posts, name="category_posts"),
]
