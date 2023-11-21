from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import AddRecord

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ""
        self.fields['username'].help_text =''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text =''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text =''



class addRecordForm(forms.ModelForm):
    first_name = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    phone = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    city = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    state = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'State '}))

    class Meta:
        model = AddRecord
        exclude = ('User',)
