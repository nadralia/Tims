from django.forms import ModelForm

from .models import Itinerary

class ItineraryForm(ModelForm):
    class Meta:
        model = Itinerary
        fields = ['itineraryname', 'numberadults', 'numberchildren', 'monthyear']

    def __init__(self, *args, **kwargs):
        super(ItineraryForm, self).__init__(*args, **kwargs)
        self.fields['itineraryname'].widget.attrs['class'] =  'input'
        self.fields['numberadults'].widget.attrs['class'] = 'select'
        self.fields['numberchildren'].widget.attrs['class'] = 'select'
        self.fields['monthyear'].widget.attrs['class'] = 'date'