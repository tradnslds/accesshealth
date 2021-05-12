from django import forms 
from .models import Department

class employeeForm(forms.ModelForm): 


    class Meta: 
        # specify model and field to be used 
        model = Department 
        fields = '__all__ '