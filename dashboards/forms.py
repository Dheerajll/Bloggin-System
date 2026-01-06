from django import forms
from Blogs.models import *
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
