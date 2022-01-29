from django.shortcuts import render
from .models import Author, Book
from .forms import BookFormSet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request: HttpRequest):
    return HttpResponse('welcome to index')



def create_book(request: HttpRequest, pk):
    author = Author.objects.get(pk=pk)
    formset = BookFormSet(request.POST or None)


    if request.method == 'POST':
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create-book", pk=author.id)

    context = {
        "formset": formset,
        "author": author
    }

    return render(request, 'create_book.html', context)