from django.urls import path
from .views import (UserProfileListCreateAPIView, UserProfileRetrieveUpdateDestroyAPIView, stream_response, \
                    CountWordsView, CategoryListCreateAPIView, PostCreateAPIView, CommentCreateAPIView, PostListAPIView)

urlpatterns = [
    path('profiles/', UserProfileListCreateAPIView.as_view(),
         name='profile-list-create'),

    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(),
         name='profile-retrieve-update-destroy'),

    path('stream/', stream_response, name='stream-response'),

    path('count-words/', CountWordsView.as_view(), name='count-words'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),

    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('comments/create/', CommentCreateAPIView.as_view(), name='comment-create'),
]
