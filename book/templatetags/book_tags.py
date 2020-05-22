from django import template

from book.models import Book


register = template.Library()



def get_book_item_category(order, count):
    """QuerySet post item"""
    post = Book.objects.filter(

            category__published=True,
            published=True
        ).order_by(order)
    if count is not None:
        post = post[:count]
    return post


@register.inclusion_tag('inc/tags/base_tag.html', takes_context=True)
def book_item(context, template = 'inc/tags/book/books_tag.html', order='-id', count=None):
    """Вывод posta в шаблон"""
    return {
        "template": template,
        "items": get_book_item_category( order, count)
    }


@register.simple_tag(takes_context=True)
def for_book_item(context,  order='-id', count=None):
    """Вывод posta без шаблона"""
    return get_book_item_category( order, count)


