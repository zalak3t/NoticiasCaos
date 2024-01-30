from django.urls import path 
from .views import index, noticia1, noticia2 , noticia3, noticia4 , noticia5, NoticiaListView, NoticiaDetailView, NoticiaCreateView, NoticiaUpdateView, NoticiaDeleteView


urlpatterns = [
    path('', index, name='index'),
    path('noticia1', noticia1, name='noticia1'),
    path('noticia2', noticia2, name='noticia2'),
    path('noticia3', noticia3, name='noticia3'),
    path('noticia4', noticia4, name='noticia4'),
    path('noticia5', noticia5, name='noticia5'),
    path('', NoticiaListView.as_view(), name='noticia_list'),
    path('noticia/<int:pk>/', NoticiaDetailView.as_view(), name='noticia_detail'),
    path('noticia/new/', NoticiaCreateView.as_view(), name='noticia_new'),
    path('noticia/<int:pk>/edit/', NoticiaUpdateView.as_view(), name='noticia_edit'),
    path('noticia/<int:pk>/delete/', NoticiaDeleteView.as_view(), name='noticia_delete'),

]