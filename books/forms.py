from django import forms
from .models import Book , ISBN , Category
from django.core.exceptions import ValidationError
class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = "__all__"
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) <=10 or len(title) >=50 :
            raise ValidationError('The title Must be between 10 and 50 characters')
        return title

    

class ISBNForm(forms.ModelForm):
       class Meta:
        model = ISBN
        fields = "__all__"
        
class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
    def clean_category(self):
        category = self.cleaned_data.get('name')
      
        if len(category) < 2 :
            raise ValidationError('the category Must be more than two characters')
        return category  


