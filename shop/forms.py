from django import forms

class SearchForm(forms.Form):
    search_phrase = forms.CharField(widget=forms.TextInput)
