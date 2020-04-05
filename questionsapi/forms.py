from django.forms import ModelForm
from .models import subjects,Questions

class QCreate(ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

class SubCreate(ModelForm):
    class Meta:
        model = subjects
        fields = '__all__'