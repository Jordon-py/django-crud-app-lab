from django import forms
from .models import Snippet, Category

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'language', 'code_text', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


# # Create your views here.
# def home(request):
#     return HttpResponse('Hello, Django!')
#
# # Snippet views
# def snippet_list(request):
#     snippets = Snippet.objects.all()
#     return render(request, 'snippet_list.html', {'snippets': snippets})
#
# def snippet_detail(request, pk):
#     snippet = Snippet.objects.get(pk=pk)
#     return render(request, 'snippet_detail.html', {'snippet': snippet})
# Compare this snippet from CodeArch/views.py:
# from django.shortcuts import render, redirect
# from django.http import HttpResponse                              