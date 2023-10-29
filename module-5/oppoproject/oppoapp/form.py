from django import forms
from .models import addproduct,productaddreal

class product_form(forms.ModelForm):
    class Meta:
        model=addproduct
        fields='__all__'

class product_f(forms.ModelForm):
    class Meta:
      model=productaddreal
      fields='__all__'

    