from django.shortcuts import render
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogListView(ListView):
    queryset = Post.objects.filter(published_date__isnull=False).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    queryset = Post.objects.filter(published_date__isnull=False).order_by(
        "-published_date"
    )
    template_name = "blogging/detail.html"
