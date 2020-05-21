from django import forms
from cities.models import City_Detail

class City_Detail_Form(forms.ModelForm):
    class Meta():
        model = City_Detail
        fields = ('city_detail', 'geometry')
