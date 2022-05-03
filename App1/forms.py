from django import forms

class UserForm(forms.Form):

    name = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    age = forms.IntegerField()
    email = forms.EmailField()

class GamesForm(forms.Form):

    name = forms.CharField(max_length=30)
    developer = forms.CharField(max_length=30)
    popularity = forms.IntegerField()
    type = forms.CharField()

class CreatorsForm(forms.Form):

    username = forms.CharField(max_length=30)
    platforms = forms.CharField(max_length=30)
    subscriptions = forms.IntegerField()    