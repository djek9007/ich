from django.db import models
from django.utils import timezone
# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class CategoryBook(MPTTModel):
    """Класс модели категорий книг"""
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("url", max_length=100)
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
        verbose_name = "Категория книг"
        verbose_name_plural = "Категории книг"

class CategoryAuthor(MPTTModel):
    """Класс модели категорий книг"""
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("url", max_length=100)
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
        verbose_name = "Категория людей"
        verbose_name_plural = "Категории людей"




class AuthorBook(models.Model):
    name = models.CharField('ФИО автора', max_length=150)
    image = models.ImageField("Фото автора", upload_to="author/", null=True, blank=True)
    text = models.TextField('Описание')
    category = models.ForeignKey(CategoryAuthor, verbose_name='Категория',on_delete=models.PROTECT )

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class TagBook(models.Model):
    """Модель тегов"""
    name = models.CharField('Название тега', max_length=100, unique=True)
    slug = models.SlugField('url', max_length=100, unique=True)
    published = models.BooleanField("отображать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Теги книг"
        verbose_name_plural = "Теги книг"


class Book(models.Model):
    """Класс модели книг"""
    authors = models.ManyToManyField(AuthorBook, verbose_name='Автор(ы)')
    title = models.CharField("Наименование", max_length=500)
    slug = models.SlugField("url (книги, сборника, журнала)", max_length=100, unique=True)
    text = models.TextField("Описание")
    pages = models.PositiveIntegerField('Количество страниц', default=0)
    years = models.PositiveIntegerField('Год выпуска')
    file = models.FileField('Книга', upload_to="books/", blank=True)
    url = models.CharField("url на внешний ресурс", max_length=255, null=True, blank=True)
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
    image = models.ImageField("Главная фотография", upload_to="books_img/")
    category = models.ForeignKey(
        CategoryBook,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)
    views = models.PositiveIntegerField("Просмотрено", default=0)
    tag = models.ManyToManyField(TagBook, verbose_name='Теги', blank=True, null=True)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = "Книги, журналы, сборники"
        verbose_name_plural = "Книги, журналы, сборники"

    def name_tag(self):
        return '\n, \n '.join([str(child.name) for child in self.tag.all()])

    name_tag.short_description = 'Теги книг'


