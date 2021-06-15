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
                  'pdf', 'image', 
                  'genre', 'featured',
                  'reading_time_mins',)
        
    def __init__(self, *args, **kwargs):
        """
        Edit placeholders and labels for some inputs
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title*',
            'description': 'Enter description*',
        }

        for field in placeholders.keys():
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            
        self.fields['reading_time_mins'].label = 'Reading Time (Minutes)'
        self.fields['pdf'].label = 'PDF*'
        self.fields['genre'].label = 'Select genre'
        self.fields['title'].widget.attrs['autofocus'] = True

    