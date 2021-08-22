from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index_templates, name="index_templates"),#リンクを追加するごとに作成
    path('active/', views.index_templates1, name="index_templates1"),
=======
    path('', views.toppage, name='toppage'),
    path('blog/', views.blog, name='blog'),#リンクを追加するごとに作成
    path('blog/detail/<int:blog_id>/', views.detail, name='detail'),
>>>>>>> 0db77fd43ee90b34e8cd887f87732e8e2571d67a
]
