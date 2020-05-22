from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from .models import CategoryBook, AuthorBook,  Book, TagBook, CategoryAuthor
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
# class CategoryBookAdmin()

class ActionPublish(admin.ModelAdmin):
    """Action для публикации и снятия с публикации"""

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    def publish(self, request, queryset):
        """Опубликовать"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)

class AuthorAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(required=False, label="Содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = AuthorBook
        fields = '__all__'




class BookInline(admin.TabularInline):
    model = Book.authors.through
    verbose_name_plural = 'Связанные к автору книги, журналы, сборники'
    verbose_name = 'Связанные книги, журнал, сборник'
    
    # BookInline.short_description ='Связанные книги'
class CategoryAuthorAdmin(ActionPublish, MPTTModelAdmin):
    """Категории людей"""
    list_display = ( "name", "slug", "published", 'id',)
    list_display_links = ("name",)
    list_filter = ("parent", )
    actions = ['unpublish', 'publish']
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 20

class AuthorBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photo', 'category', )
    form = AuthorAdminForm
    search_fields = ('name', 'text',)
    fields = ('name', 'category','image', 'get_photo', 'text',)
    readonly_fields = ('get_photo',)
    # inlines = [BookInline,]
    list_filter = ('category',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Фото автора'

class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'published','id',)
    prepopulated_fields = {'slug': ('name',)}
    actions = ['unpublish', 'publish']


class BookAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(required=False, label="Содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = AuthorBook
        fields = '__all__'

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',   'pages', 'years', 'category', 'name_tag','get_photo',  'published', 'views',)
    readonly_fields = ('views', 'edit_date','get_photo', )
    form = BookAdminForm
    fields = ('title', 'slug', 'authors', 'text', 'pages', 'years', 'category','tag', 'url', 'image', 'get_photo', 'published', 'views', )
    search_fields = ('title', )
    list_editable = ('published',)
    save_on_top = True
    list_per_page = 50  # разделение записи
    list_filter = ('category',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'





class TagBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'published',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CategoryBook, CategoryBookAdmin)
admin.site.register(AuthorBook, AuthorBookAdmin)
admin.site.register(TagBook, TagBookAdmin)

admin.site.register(Book, BookAdmin)
admin.site.register(CategoryAuthor, CategoryAuthorAdmin)
