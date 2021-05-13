from django.forms import ModelForm
from .models import *


class NameForm(ModelForm):
    class Meta:
        model = CustomComputer
        fields=['name']