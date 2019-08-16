from django import template
from app.models import Post

register = template.Library()


@register.inclusion_tag('app/includes/month_links.html')
def render_month_links():
    # 未来の記事がある年・月も表示する場合は、`Post.objects.dates('created_at', 'month', order='DESC'),
    return {
        'dates': Post.objects.published().dates('created_at', 'month', order='DESC'),
    }
