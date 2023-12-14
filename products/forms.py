from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.files.images import get_image_dimensions
from products.models import Products


def validate_image(fieldfile_obj):
    w, h = get_image_dimensions(fieldfile_obj)
    if w < 300 or h < 300:
        raise ValidationError(_("Изображение должно иметь не менее 300x300 пикселей."))
class CreateProductForm(forms.Form):
    class Meta:
        model = Products
        fields = 'title', 'description', 'image'

    title = forms.CharField(label='Название',widget=forms.ClearableFileInput(attrs={'multiple': False}), validators=[validate_image], required=False)
    description = forms.CharField(label='Описание')
    image = forms.ImageField(label='Фото продукта')
    create = forms.DateField(label='Время добавления', widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY'}))

    def save(self):
        if not self.is_valid():
            raise forms.ValidationError("Ошибка валидации данных.")