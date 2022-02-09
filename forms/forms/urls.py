"""forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import (
    create_book,
    create_book_formset,
    index,
    create_book_form,
    detail_book,
    delete_book
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('<pk>/', create_book, name="create-book"),
    path('create-book-formset/<pk>/', create_book_formset, name="create-book-formset"),
    path('book-form', create_book_form, name="book-form"),
    path('detail-book/<pk>', detail_book, name="detail-book"),
    path('<pk>/delete-book', delete_book, name="delete-book"),
]
