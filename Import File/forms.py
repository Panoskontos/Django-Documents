from .models import Book
from django.forms import ModelForm


class UploadBook(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
