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
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail-book", pk=book.id)
        # in case of errors in the form, return partial template
        else:
            return render(request, 'partials/book_form.html', {"form": form})

    # if book not created, return create book template
    context = {
        "form": form,
        "author": author,
        "books": books,
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


# return book details, used with htmx
def detail_book(request: HttpRequest, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }
    return render(request, "partials/book_detail.html", context)


def delete_book(request: HttpRequest, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse('')


def update_book(request: HttpRequest, pk):
    book = Book.objects.get(pk=pk)
    # make to sure to pass the post request if there's one
    form = BookForm(request.POST or None, instance=book)

    # user clicked on submit button
    if request.method == 'POST':
        if form.is_valid():
            book.save()
            return redirect("detail-book", pk=book.id)

    # user clicked on update button
    context = {
        "form": form,
        "book": book
    }
    return render(request, "partials/book_form.html", context)
