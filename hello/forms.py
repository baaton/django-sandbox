from django import forms

class AddPost(forms.Form):
    title = forms.CharField(label='Article title', max_length=50)
    body = forms.CharField(widget=forms.Textarea(attrs={'id': 'editor'}))