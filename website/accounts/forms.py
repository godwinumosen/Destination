from django import forms


class ProductDestinatinForm(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    username=forms.CharField(max_length=50)
    password1=forms.CharField(max_length=50)
    password2=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)
    
    def __str__(self):
        return self.first_name