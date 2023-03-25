from django.forms import ModelForm
from django import forms
from .models import Enquiry, Subscribtion,Contact




class Enquiry(ModelForm):
    Product = forms.CharField(widget=forms.HiddenInput())
    name  = forms.TextInput()
    mobile_number  = forms.IntegerField()
    email = forms.TextInput()
    location = forms.TextInput()
    requirment = forms.TextInput()


   
    


    def __init__(self,*args, **kwargs):
            super().__init__(*args,**kwargs)
                   
            self.fields['name'].widget.attrs.update(
                {
                'class': 'form-control mb-3',
                'placeholder' : 'Full Name*'
            
                })
            self.fields['mobile_number'].widget.attrs.update(
                {
                'class': 'form-control mb-3',
                'placeholder' : 'Mobile Number*'
            
                })
            self.fields['email'].widget.attrs.update(
                            {
                            'class': 'form-control mb-3',
                            'placeholder' : 'Email Id*'
                        
                            })
            self.fields['location'].widget.attrs.update(
                            {
                            'class': 'form-control mb-3',
                            'placeholder' : 'Location*'
                        
                            })
            self.fields['requirment'].widget.attrs.update(
                            {
                            'class': 'form-control mb-3',
                            'placeholder' : 'Requirment'
                        
                            })
            self.fields['Product'].widget.attrs.update(
                            {
                            'class': 'form-control mb-3',
                            'placeholder' : 'Product',
                            
                        
                            })

    class Meta:
        model = Enquiry
        fields = ['Product','name','mobile_number', 'email' , 'location','requirment']



class Subscribtion(ModelForm):
    
    email = forms.EmailField()   
    


    def __init__(self,*args, **kwargs):
            super().__init__(*args,**kwargs)
                   
            
            self.fields['email'].widget.attrs.update(
                            {
                            'class': 'form-control rounded-0 border-0 mr-3 mb-4 mb-sm-0',
                            'placeholder' : 'Email Id*',
                            'name' : 'email',
                            'type': 'email',
                            
                        
                            })
                           

    class Meta:
        model = Subscribtion
        fields = ['email']


class contact_form(ModelForm):
    
    first_name  = forms.TextInput()
    last_name  = forms.TextInput()
    email = forms.EmailField()   
    message  = forms.TextInput()
    


    def __init__(self,*args, **kwargs):
            super().__init__(*args,**kwargs)
                   
            
            self.fields['first_name'].widget.attrs.update(
                            {
                            'class': 'form-control mb-4 rounded-0',
                            'placeholder' : 'First Name*',
                            'name' : 'first_name',
                            
                            
                        
                            })
            self.fields['last_name'].widget.attrs.update(
                            {
                            'class': 'form-control mb-4 rounded-0',
                            'placeholder' : 'Last Name*',
                            'name' : 'last_name',
                            
                            
                        
                            })
            
            self.fields['email'].widget.attrs.update(
                            {
                            'class': 'form-control mb-4 rounded-0',
                            'placeholder' : 'Email Id*',
                            'name' : 'email',
                            
                            
                        
                            })
            
            self.fields['message'].widget.attrs.update(
                            {
                            'class': 'form-control mb-4 rounded-0',
                            'placeholder' : 'Message*',
                            'name' : 'message',
                            
                            
                        
                            })
                           

    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','message']