from django import forms

from .models import Story


class StoryForm(forms.ModelForm):
    """
    ModelForm subclass which helps implement UI
    for create/edit story form on story page
    """
    class Meta:
        model = Story
        fields = ('title', 'description',
                  'image', 'pdf',
                  'genre', 'featured',
                  'reading_time_mins',)
        
    def __init__(self, *args, **kwargs):
        """
        Edit placeholders and labels for some inputs
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Enter a description of the story...',
        }

        for field in placeholders.keys():
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            
        self.fields['reading_time_mins'].label = 'Reading Time (Minutes)'
        self.fields['title'].widget.attrs['autofocus'] = True

    