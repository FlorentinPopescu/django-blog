""" bloggings/views.py script """

# imports
from django.shortcuts import render
from django.http import Http404  # HttpResponse, HttpResponseRedirect
# from django.template import loader

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from blogging.models import Post
# ------------------------------------


def list_view(request):
    """ list view """
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('published_date')
    context = {'posts': posts}
    # template = loader.get_template('blogging/list.html')
    # body = template.render(context)
    # return HttpResponse(body, content_type="text/html")
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    """ detail view """
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
# --------------------------------------


class PostUpdateView(UpdateView):
    """ update post """
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text', 'published_date']
 

class PostDeleteView(DeleteView):
    """ delete post """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog_index')
    
# --------------------------------------
