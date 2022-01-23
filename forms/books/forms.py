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


BookForm = inlineformset_factory(
    parent_model=Author,
    model=Book,
    form=BookForm,
    can_delete=True,
    min_num=2,  # minimum books to enter
    extra=0  # extra forms to show (for empty forms)
)
