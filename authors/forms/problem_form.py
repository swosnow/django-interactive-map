from utils.django_forms import add_attr
from collections import defaultdict
from django.core.exceptions import ValidationError
from django import forms
from mapaguapi.models import Problem


class AuthorProblemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)
        

        
        


    class Meta:
        model = Problem
        fields = 'title', 'description', 'cep'

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        if len(title) < 5:
            self._my_errors['title'].append('Deve possuir pelo menos 5 letras')
        
        if title == description:
            self._my_errors['title'].append('Não pode ser igual a descrição')
            self._my_errors['description'].append('Não pode ser igual ao título')
        
        
        if self._my_errors:
            raise ValidationError(self._my_errors)
        return super_clean