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
    parent_model=Author,
    model=Book,
    form=BookForm,
    can_delete=True, # show / hide delete buttons
    min_num=2,  # minimum books to enter
    extra=0  # extra forms to show (for empty forms)
)
