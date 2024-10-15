from django.forms import ModelForm, BooleanField
from catalog.models import Product, Version
from django.core.exceptions import ValidationError


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):

    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        exclude = ("views_counter",)


    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]
        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise ValidationError(
                    "Наименование продукта содержит недопустимые слова."
                )
        return cleaned_data


    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]
        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise ValidationError(
                    "Описание продукта содержит недопустимые слова."
                )
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"