from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Snippet CRUD
    path('snippets/', views.snippet_list, name='snippet_list'),
    path('snippets/create/', views.snippet_create, name='snippet_create'),
    path('snippets/<int:pk>/', views.snippet_detail, name='snippet_detail'),
    path('snippets/<int:pk>/update/', views.snippet_update, name='snippet_update'),
    path('snippets/<int:pk>/delete/', views.snippet_delete, name='snippet_delete'),

    # Category CRUD
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
]
