""" blogging/urls.py script """

# imports
from django.urls import path

from blogging.views import list_view, detail_view
from blogging.views import PostUpdateView, PostDeleteView
# ----------------------------------
 

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),

    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    ]

