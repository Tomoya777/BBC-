from django.urls import path

from . import views

urlpatterns = [
    path('', views.toppage, name='toppage'),
    path('blog/', views.blog, name='blog'),#リンクを追加するごとに作成
]
