from django.forms import ModelForm
from apartments.models import Apartment

class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['nickname', 'building', 'description', 'price', 'leasingOptions', 'bedrooms']
        
