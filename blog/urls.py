from django.urls import path
from .views import Home, News

app_name = 'blog'
urlpatterns = [
    path('news/', News.as_view(), name='news'),
    path('', Home.as_view(), name='home'),

]
