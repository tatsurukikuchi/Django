# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.urls import reverse_lazy
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post


class PostDetail(generic.DetailView):
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('myapp:post_list')


class PostUpdate(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('myapp:post_list')


class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('myapp:post_list')
