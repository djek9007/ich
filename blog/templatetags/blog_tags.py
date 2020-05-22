from django import template

from blog.models import Post


register = template.Library()

@register.inclusion_tag('inc/tags/blog/4_most_popular_tag.html')
def get_popular(count=10):
    posts = Post.objects.order_by('-views')[:count]
    return {"items": posts}


def get_post_item_category(category, order, count):
    """QuerySet post item"""
    post = Post.objects.filter(
            category_id=category,
            category__published=True,
            published=True
        ).order_by(order)
    if count is not None:
        post = post[:count]
    return post


@register.inclusion_tag('inc/tags/base_tag.html', takes_context=True)
def post_item(context, category, template = 'inc/tags/blog/1_post_tag_main.html', order='-id', count=None):
    """Вывод posta в шаблон"""
    return {
        "template": template,
        "items": get_post_item_category(category, order, count)
    }


@register.simple_tag(takes_context=True)
def for_post_item(context, category, order='-id', count=None):
    """Вывод posta без шаблона"""
    return get_post_item_category(category, order, count)


