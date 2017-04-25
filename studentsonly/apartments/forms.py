from django.forms import ModelForm
from apartments.models import Apartment, Reviews

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'building', 'comment', 'hospitality', 'maintenance', 'safety_security', 'overall']
 
class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['nickname', 'building', 'description', 'price', 'leasingOptions', 'bedrooms']
        
