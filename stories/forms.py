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
                  'image_credit',
                  'genre', 'featured',
                  'reading_time_mins',)
        
    def __init__(self, *args, **kwargs):
        """
        Edit labels
        """
        super().__init__(*args, **kwargs)

        labels = {
            'title': 'Title',
            'description': 'Description',
            'reading_time_mins': 'Reading time (mins)',
            'pdf': 'PDF',
            'image': 'Image',
            'image_credit': 'Image credit',
            'genre': 'Genre',
            'featured': 'Featured',
        }

        for field in self.fields:
            self.fields[field].widget.attrs.pop("autofocus", None)

        for field in labels.keys():
            self.fields[field].label = labels[field]

        current_classes = self.fields['genre'].widget.attrs.get('class', '')
        if current_classes:
            self.fields['genre'].widget.attrs.update({'class': f'{current_classes} form-select'})
        else:
            self.fields['genre'].widget.attrs['class'] = 'form-select'
