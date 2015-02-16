from django import forms

class AddPost(forms.Form):
    title = forms.CharField(label='Article title',
                            max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Your Article',
                           widget=forms.Textarea(attrs={'id': 'editor', 'class': 'form-textarea form-control'}))

class AddComment(forms.Form):
    user_name = forms.CharField(label='Your Name',
                                max_length=250,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Your Comment',
                           widget=forms.Textarea(attrs={'class': 'form-control form-comment'}))