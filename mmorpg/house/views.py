from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Post, Comment
from .forms import PostForm


class HousePage(ListView):
    model = Post
    ordering = 'title_name'
    template_name = "housetemp/housepage.html"
    context_object_name = 'Posts'


class PostCreate(CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'housetemp/post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'housetemp/post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('h_page')
