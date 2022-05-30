from django import forms

from .models import Book

import pandas as pd

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf','cover')
        
