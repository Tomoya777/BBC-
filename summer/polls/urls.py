from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_templates, name="index_templates"),#リンクを追加するごとに作成
]
