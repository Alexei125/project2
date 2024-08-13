from django.forms import ModelForm

from catalog.models import Product
from items.forms import StyleFormMixin


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description')
