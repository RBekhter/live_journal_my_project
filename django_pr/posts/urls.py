from django.urls import path



urlpatterns = [
    path('posts/', posts.views.posts_view)
]