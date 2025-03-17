from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Snippet, Category
from .forms import SnippetForm, CategoryForm

def home(request):
    return render(request, 'home.html')

def snippet_list(request):
    snippets = Snippet.objects.all().order_by('-created_at')
    return render(request, 'snippet_list.html', {'snippets': snippets})

def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippet_detail.html', {'snippet': snippet})

@login_required
def snippet_create(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.owner = request.user
            snippet.save()
            return redirect('snippet_detail', pk=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, 'snippet_create.html', {'form': form})

@login_required
def snippet_update(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippet_detail', pk=snippet.pk)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippet_update.html', {'form': form})

@login_required
def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, owner=request.user)
    if request.method == 'POST':
        snippet.delete()
        return redirect('snippet_list')
    return render(request, 'snippet_delete.html', {'snippet': snippet})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        # Only staff can delete categories, e.g.:
        if request.user.is_staff:
            category.delete()
        return redirect('category_list')
    return render(request, 'category_delete.html', {'category': category})
