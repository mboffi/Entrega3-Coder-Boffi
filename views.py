from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django_filters.views import FilterView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Editorial, Genero, Idioma, Libro
from .forms import EditorialForm, GeneroForm, IdiomaForm, LibroForm, BusquedaForm
from .filters import LibroFilter

class EditorialListView(ListView):
    model = Editorial
    template_name = 'biblioteca/editoriales.html'

class EditorialCreateView(CreateView):
    model = Editorial
    form_class = EditorialForm
    success_url = reverse_lazy('editoriales')
    template_name = 'biblioteca/editorial_form.html'

class GeneroListView(ListView):
    model = Genero
    template_name = 'biblioteca/generos.html'

class GeneroCreateView(CreateView):
    model = Genero
    form_class = GeneroForm
    success_url = reverse_lazy('generos')
    template_name = 'biblioteca/genero_form.html'

class IdiomaListView(ListView):
    model = Idioma
    template_name = 'biblioteca/idiomas.html'

class IdiomaCreateView(CreateView):
    model = Idioma
    form_class = IdiomaForm
    success_url = reverse_lazy('idiomas')
    template_name = 'biblioteca/idioma_form.html'

class LibroListView(FilterView):
    model = Libro
    filterset_class = LibroFilter
    template_name = 'biblioteca/libros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaForm(self.request.GET)
        return context

class LibroCreateView(View):
    def get(self, request):
        editorial_form = EditorialForm()
        genero_form = GeneroForm()
        idioma_form = IdiomaForm()
        libro_form = LibroForm()
        return render(request, 'biblioteca/libro_form.html', {'editorial_form': editorial_form, 'genero_form': genero_form, 'idioma_form':
