from django.urls import path
from .views import EditorialListView, EditorialCreateView, GeneroListView, GeneroCreateView, IdiomaListView, IdiomaCreateView, LibroListView, LibroCreateView, search

urlpatterns = [
    path('editoriales/', EditorialListView.as_view(), name='editoriales'),
    path('editorial/add/', EditorialCreateView.as_view(), name='editorial_add'),
    path('generos/', GeneroListView.as_view(), name='generos'),
    path('genero/add/', GeneroCreateView.as_view(), name='genero_add'),
    path('idiomas/', IdiomaListView.as_view(), name='idiomas'),
    path('idioma/add/', IdiomaCreateView.as_view(), name='idioma_add'),
    path('libros/', LibroListView.as_view(), name='libros'),
    path('libro/add/', LibroCreateView.as_view(), name='libro_add'),
    path('search/', search, name='search'),
]
