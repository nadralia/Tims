from django.forms import ModelForm

from .models import Inquiry

class InquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = ['title', 'description', 'inquirystatus']
    
    def __init__(self, *args, **kwargs):
        super(InquiryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] =  'input'
        self.fields['description'].widget.attrs['class'] = 'textarea'
        self.fields['inquirystatus'].widget.attrs['class'] = 'select'

