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
                  'genre', 'featured',)

        # add hour and min form inputs for reading time
        reading_time_hours = forms.IntegerField(max_value=1000, min_value=0)
        reading_time_minutes = forms.IntegerField(max_value=59, min_value=0)
        

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
        
        self.fields['title'].widget.attrs['autofocus'] = True

    