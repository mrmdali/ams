from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('full_name', 'phone', 'type_of_service', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({
            'type': 'text',
            'name': 'Full Name',
            'placeholder': 'Full Name',
            'onfocus': 'this.placeholder="" ',
            'onblur': 'this.placeholder="Full Name" ',
            'required': 'required',
            'class': 'single-input-primary',
        })
        self.fields['phone'].widget.attrs.update({
            'type': 'text',
            'name': 'Phone Number',
            'placeholder': 'Phone Number',
            # 'onfocus': 'this.placeholder="" ',
            'autocomplete':'phone',
            'aria-label':'989292992',
            # 'onblur': 'this.placeholder="Phone Number" ',
            'required': 'required',
            'class': 'single-input-primary',
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Message',
            'onfocus': 'this.placeholder="" ',
            'onblur': 'this.placeholder="Message" ',
            'class': 'single-textarea',
        })
