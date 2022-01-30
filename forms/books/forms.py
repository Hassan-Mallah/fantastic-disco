from django import forms
from django.forms.models import inlineformset_factory
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "number_of_pages"
        )


BookFormSet = inlineformset_factory(
    Author,
    Book,
    form=BookForm,
    min_num=2,  # minimum books to enter
    extra=1,  # extra forms to show (for empty forms)
    can_delete=False # show / hide delete buttons
)
