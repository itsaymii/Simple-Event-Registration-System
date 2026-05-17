from django import forms
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['full_name', 'email', 'age', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'yourname@gmail.com'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age',
                'min': '18'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Create a password (min 8 characters)'
            }),
        }
    
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if len(full_name.strip()) < 5:
            raise forms.ValidationError("Full name must be at least 5 characters long.")
        return full_name.strip()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must end with @gmail.com")
        return email.lower()
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("You must be 18 years or older to register.")
        return age
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password