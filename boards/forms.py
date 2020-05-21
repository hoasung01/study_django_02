from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?', 'class': 'form-control'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    subject = forms.CharField(
        widget = forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']