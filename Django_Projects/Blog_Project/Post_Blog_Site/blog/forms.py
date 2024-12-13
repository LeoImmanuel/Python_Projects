from django import forms
from blog.models import Post, Comment

# Creating a post form view
class PostForm(forms.ModelForm):
    class Meta():
        # connection to the post model
        model = Post
        # Edit fields
        fields = ('author','title','text')

        # Editing/Styling form widgets
        widgets ={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

# Creating a comment form view for each blog post
class CommentForm(forms.ModelForm):
    class Meta():
        # Connection to Comment Model
        model = Comment
        fields = ('author','text')

        # Editing/Styling form widgets
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }