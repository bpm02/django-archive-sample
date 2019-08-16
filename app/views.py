from django.views import generic
from .models import Post


class PostArchiveMixin:
    """ArchiveView関連で使うMixin。主要な属性をこちらにまとめた。"""
    model = Post
    paginate_by = 10
    date_field = 'created_at'
    template_name = 'app/post_list.html'
    allow_empty = True
    make_object_list = True
    # allow_future = True  # 未来の記事を表示する場合はこれがいる


class PostArchiveIndex(PostArchiveMixin, generic.ArchiveIndexView):
    """トップページ、全記事一覧"""
    pass


class PostYearArchiveIndex(PostArchiveMixin, generic.YearArchiveView):
    """年別の記事"""
    pass


class PostMonthArchiveIndex(PostArchiveMixin, generic.MonthArchiveView):
    """月別の記事"""
    month_format = '%m'


class PostDetail(generic.DetailView):
    """記事の詳細"""
    model = Post
