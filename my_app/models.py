from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Snippet(models.Model):
    LANGUAGE_CHOICES = [
        ('JS', 'JavaScript'),
        ('PY', 'Python'),
        ('CSS', 'CSS'),
    ]
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES, default='PY')
    code_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='snippets')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
# Compare this snippet from CodeArch/views.py:
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Snippet, Category
# from .forms import SnippetForm, CategoryForm
#
# # Create your views here.
# def home(request):
#     return HttpResponse('Hello, Django!')
#
# # Snippet views                   
