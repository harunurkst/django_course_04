from django.urls import path
from .views import *


urlpatterns = [
    path('posts', post_list, name='post-list'),
    path('posts/create', create_post, name='post-create'),
    path('detail/<slug>', post_detail, name='post-detail'),
    path('authors', author_list, name='authors'),
    path('authors/<author_name>', authors_post, name='author-post'),
]