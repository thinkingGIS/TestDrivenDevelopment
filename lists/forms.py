from django import forms

from lists.models import Item

EMPTY_LIST_ERROR = "You can't have an empty list item Madafaka!"

class ItemForm(forms.models.ModelForm):
    """docstring for ItemForm"""

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }