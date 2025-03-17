# Compare this snippetfrom CodeArch/views.py:
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Snippet, Category
from .forms import SnippetForm, CategoryForm

# Create your views here.
def home(request):
     return HttpResponse('Hello, Django!')

# Snippet views
def snippet_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippet_list.html', {'snippets': snippets})               
