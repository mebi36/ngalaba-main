from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Author, Post, Post_Section
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """
        Return the last five published posts

        """
        return Post.objects.order_by('-post_date')[:5]
class PostDetailView(generic.DetailView):
    model = Post


class AuthorDetailView(generic.DetailView):
    model = Author