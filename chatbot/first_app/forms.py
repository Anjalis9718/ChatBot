from django import forms
class PostForm(forms.Form):

    text=forms.CharField(max_length=80,widget=forms.TextInput(attrs={
				   'id':'posttext','name':'post','size': 30}))
