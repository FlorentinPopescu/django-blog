""" bloggings/views.py script """

# imports
from datetime import datetime
from django.shortcuts import render, get_object_or_404
# from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.template import loader

from django.views import generic
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin) 
from django.contrib.auth import get_user_model

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
    # try:
    #     post = published.get(pk=post_id)
    # except Post.DoesNotExist:
    #     raise Http404
    post =  get_object_or_404(published, pk=post_id)
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
# --------------------------------------


class CustomUserCreationForm(UserCreationForm):
    """ custom user creation form """
    class Meta:
        """ meta """
        model = get_user_model()
        fields = ('email', 'username', )


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login') 
    template_name = 'signup.html'
# --------------------------------------


class PostCreateView(LoginRequiredMixin, CreateView):
    """ create view """
    model = Post
    template_name = "post_create.html"
    login_url = "login"    
    published_date = datetime.now()
    fields = ('title', 'text', 'published_date', )
    
    def form_valid(self, form):
         """ form valid """
         form.instance.author = self.request.user
         return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ update post """
    model = Post
    template_name = 'post_edit.html'
    login_url = "login"
    fields = ('title', 'text', 'published_date', )
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ delete post """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog_index')
    login_url = "login"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
# --------------------------------------
 