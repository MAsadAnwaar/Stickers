from django import forms
from .models import StickerList

# forms.py
from multiupload.fields import MultiFileField

class StickerListForm(forms.Form):
    sticker = MultiFileField(min_num=1)
    # sticker = MultiFileField(min_num=1, max_num=10)


