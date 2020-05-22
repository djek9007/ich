from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from datetime import datetime
from blog.models import Post


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'

class News(ListView):
    model = Post
    template_name = 'blog/news.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return  Post.objects.filter(published=True, published_date__lte=datetime.now(), category_id=3).order_by('-published_date')

