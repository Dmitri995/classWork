from django.forms import Form, ModelForm
from .models import Book

class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = '__all__'