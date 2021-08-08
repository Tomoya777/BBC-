from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name="blog"),#リンクを追加するごとに作成
]
