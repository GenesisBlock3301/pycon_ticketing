from django import forms

class TicketForm(forms.Form):
    name = forms.CharField(min_length=2,widget=forms.TextInput(attrs={'class':'input' ,'placeholder':'Enter your full name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter Email'}))
    # phone = forms.CharField(min_length=11,max_length=11,widget=forms.TextInput({'class':'input'}))
    phone = forms.RegexField(regex=r'^017',widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter your phone number'}))