from django import forms
from .models import News
from django.contrib.admin.widgets import AdminDateWidget

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'created_at']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'created_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }