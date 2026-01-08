from django import forms
from website.models import Contact,Newsleter

class NameForm(forms.Form):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

class NewsleterForm(forms.ModelForm):

    class Meta:
        model = Newsleter
        fields = ['email']