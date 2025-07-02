from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from catalog.models import Category, Product

DICT = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class CategoryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name:
            self.validate_forbidden_words(name)
        if description:
            self.validate_forbidden_words(description)

        return cleaned_data

    def validate_forbidden_words(self, value):
        for word in DICT:
            if word.lower() in value.lower():
                raise forms.ValidationError(f"Слово '{word}' запрещено использовать.")

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is not None and price <= 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")

        return price
