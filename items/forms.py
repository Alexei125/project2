from django import forms
from django.forms import ModelForm

from catalog.models import Product
from items.models import Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-check-input'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
            'бесплатно', 'обман', 'полиция', 'радар') in cleaned_data:
            raise forms.ValidationError('Не могут создавать продукты с запрещенными словами ')

        return cleaned_data


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = ['number_version', 'name_version', 'current_version']
