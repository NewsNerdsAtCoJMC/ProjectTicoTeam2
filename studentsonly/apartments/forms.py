from django.forms import ModelForm
from apartments.models import People, Apartment

class PeopleForm(ModelForm):
    class Meta:
        model = People
        exclude = ['user']
        
class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['nickname', 'building', 'description', 'price', 'leasingOptions', 'bedrooms']