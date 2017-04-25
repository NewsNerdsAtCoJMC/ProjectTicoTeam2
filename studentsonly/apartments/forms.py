from django.forms import ModelForm
from apartments.models import Apartment, Reviews

class ApartmentForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'building', 'comment', 'hospitality', 'maintenance', 'saftey_security', 'overall']
    
    class Meta:
        model = Apartment
        fields = ['nickname', 'building', 'description', 'price', 'leasingOptions', 'bedrooms']
        
