from django.shortcuts import render
from .models import Author, Book
from .forms import BookFormSet, BookForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request: HttpRequest):
    return HttpResponse('welcome to index')


def create_book(request: HttpRequest, pk):
    author = Author.objects.get(pk=pk)
    form = BookForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail-book", pk=author.id)
        # in case of errors in the form, return partial template
        else:
            return render(request, 'partials/book_form.html', {"form": form})

    # if book not created, return create book template
    context = {
        "form": form,
        "author": author,
    }

    return render(request, 'create_book.html', context)


# not part of the tutorial, using formset
def create_book_formset(request: HttpRequest, pk):
    author = Author.objects.get(pk=pk)
    formset = BookFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create-book", pk=author.id)

    context = {
        "formset": formset,
        "author": author,
    }

    return render(request, 'create_book.html', context)


def create_book_form(request: HttpRequest):
    context = {
        "form": BookForm()
    }
    return render(request, "partials/book_form.html", context)


def detail_book(request: HttpRequest, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }
    return render(request, "partials/book_detail.html", context)