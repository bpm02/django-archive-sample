from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostArchiveIndex.as_view(), name='top'),  # トップページ、全記事一覧
    path('archive/<int:year>/', views.PostYearArchiveIndex.as_view(), name='year'),  # 年別の記事
    path('archive/<int:year>/<int:month>/', views.PostMonthArchiveIndex.as_view(), name='month'),  # 月別の記事
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='detail'),  # 記事詳細
]
