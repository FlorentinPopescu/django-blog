""" bloggings/views.py script """

# imports
from django.shortcuts import render
from django.http import HttpResponse, Http404  #,HttpResponseRedirect

from django.template import loader
from blogging.models import Post
# ------------------------------------

def list_view(request):
    """ list view """
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
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



#def stub_view(request, *args, **kwargs):
#    """ page view """
#    body = "Stub View\n\n"
#
#    if args:
#        body += "Args:\n"
#        body += "\n".join(["\t%s" % a for a in args])
#    if kwargs:
#        body += "Kwargs:\n"
#        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#   
#    return HttpResponse(body, content_type="text/plain")

