from django import forms

class addForm(forms.Form):

    image = forms.ImageField(required=False)  
