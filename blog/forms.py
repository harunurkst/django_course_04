from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', )



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'category', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
        }
