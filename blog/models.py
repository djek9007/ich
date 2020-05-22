from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """Класс модели категорий сетей"""
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("url", max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    published = models.BooleanField("Отображать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"





class Post(models.Model):
    """Класс модели поста"""
    title = models.CharField("Заголовок", max_length=500)
    slug = models.SlugField("url", max_length=100, unique=True)
    text = models.TextField("Содержание")
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        "Дата публикации",
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField("Главная фотография", upload_to="post/")
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)
    views = models.PositiveIntegerField("Просмотрено", default=0)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']


class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField('Название тега', max_length=100, unique=True)
    slug = models.SlugField('url', max_length=100, unique=True)
    published = models.BooleanField("отображать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"