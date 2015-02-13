from django import forms

class AddPost(forms.Form):
    title = forms.CharField(label='Article title', max_length=50)
    body = forms.CharField(label='Your Article', widget=forms.Textarea(attrs={'id': 'editor'}))

class AddComment(forms.Form):
    user_name = forms.CharField(label='Your Name', max_length=250)
    body = forms.CharField(label='Your Comment', widget=forms.Textarea())