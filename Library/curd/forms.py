from django import forms
from database.models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["title", "author", "pub_data"]
