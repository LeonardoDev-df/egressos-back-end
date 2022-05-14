from django import forms

from .models import Book

import pandas as pd

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf','cover')
        pr = pd.read_csv(
            'media/Formulário de Avaliação de egressos dos cursos Técnicos Subsequentes do IFB (respostas).csv',
             encoding='latin1',
             parse_dates=['Carimbo de data/hora', 'Data de nascimento:'],
             sep=';',
             decimal=',',
             thousands='.'
        )
