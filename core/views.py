from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Noticia

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def noticia1(request):
    return render(request, 'core/noticia1.html')

def noticia2(request):
    return render(request, 'core/noticia2.html')

def noticia3(request):
    return render(request, 'core/noticia3.html')

def noticia4(request):
    return render(request, 'core/noticia4.html')

def noticia5(request):
    return render(request, 'core/noticia5.html')

class NoticiaListView(ListView):
    model = Noticia
    template_name = 'noticia_list.html'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticia_detail.html'

class NoticiaCreateView(CreateView):
    model = Noticia
    fields = ['titulo', 'contenido', 'autor', 'fecha_publicacion']
    template_name = 'noticia_form.html'
    success_url = reverse_lazy('noticia_list')

class NoticiaUpdateView(UpdateView):
    model = Noticia
    fields = ['titulo', 'contenido', 'autor', 'fecha_publicacion']
    template_name = 'noticia_form.html'
    success_url = reverse_lazy('noticia_list')

class NoticiaDeleteView(DeleteView):
    model = Noticia
    template_name = 'noticia_confirm_delete.html'
    success_url = reverse_lazy('noticia_list')
    


