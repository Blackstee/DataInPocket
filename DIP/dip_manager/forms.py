from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()



class ImageUploadForm_comm(forms.Form):
    """Image upload form."""
    image_comm = forms.ImageField()