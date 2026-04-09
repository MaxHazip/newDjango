from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Books, Authors

# Create your views here.
class Page(ListView):
    template_name = "index.html"
    model = Books
    context_object_name = "books"

class Author(DetailView):
    template_name = "author.html"
    model = Authors
    context_object_name = "author"

# class Page(ListView):
#     template_name = "index.html"
#     model = Books
#     context_object_name = "books"

#     def get_queryset(self):
#         return self.model.objects.filter(name__startswith="С")
    
# class newListView():
#     template_name = "index.html"
#     model = Books
#     context_object_name = "books"

#     allObjects = model.objects.all()

#     context = {

#         context_object_name: allObjects

#     }

#     render(request, 'main-content.html', context)