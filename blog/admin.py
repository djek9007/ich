from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from blog.models import Category, Tag, Post

class PostAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(required=False, label="Содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

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




class CategoryAdmin(ActionPublish, MPTTModelAdmin):
    """Категории блога"""
    list_display = ( "name", "parent", "slug", "published", 'id',)
    list_display_links = ("name",)
    list_filter = ("parent", )
    actions = ['unpublish', 'publish']
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 20


class PostAdmin(ActionPublish):
    """Посты блога"""
    list_display = ('title', 'published_date',  'published', 'views','id',)
    form = PostAdminForm
    fields = ('title', 'slug', 'image', 'get_photo','text', 'edit_date', 'published_date', 'category', 'published', 'views',)
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    actions = ['unpublish', 'publish']
    list_editable = ('published',)
    readonly_fields = ('views', 'edit_date', 'get_photo')
    list_filter = ('category',)
    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

