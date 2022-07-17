#from django.shortcuts import render
# from audioop import reverse
# from tkinter.ttk import LabeledScale
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "index.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body", "author"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_del.html"
    success_url = reverse_lazy("blog:home")
    # @staticmethod
    # def options_to_confirm(request):
    #     if request.POST == "Confirm":
    #         success_url = reverse("blog:new")
