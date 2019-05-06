from django import forms
from django.forms import ModelForm, Textarea
from .models import Reviews

RATING_CHOICES=[
	(1, '1'),
	(2, '2'),
	(3, '3'),
	(4, '4'),
	(5, '5'),
	]

class SearchForm(forms.Form):
    search_phrase = forms.CharField(widget=forms.TextInput)

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Reviews
		fields = ['CustomerID', 'Ratings', 'Review',]
		widgets = {
			'Review': Textarea(attrs={'cols':40, 'rows':15})
		}