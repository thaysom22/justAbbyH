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
            'title': 'Title',
            'description': 'Description',
            'reading_time_mins': 'Reading time (mins)',
        }

        labels = {
            'title': 'Title',
            'description': 'Description',
            'reading_time_mins': 'Reading time (mins)',
            'pdf': 'PDF',
            'image': 'Image',
            'genre': 'Genre',
            'featured': 'Featured',
        }
        for field in self.fields:
            self.fields[field].widget.attrs.pop("autofocus", None)

        for field in placeholders.keys():
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]

        for field in labels.keys():
            self.fields[field].label = labels[field]

        current_classes = self.fields['genre'].widget.attrs.get('class', '')
        if current_classes:
            self.fields['genre'].widget.attrs.update({'class': f'{current_classes} form-select'})
        else:
            self.fields['genre'].widget.attrs['class'] = 'form-select'
