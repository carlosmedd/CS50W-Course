from django import forms
from .models import Category

class ListingForm(forms.Form):
    title = forms.CharField(max_length=64, required=True, widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Title"}))
    
    description = forms.CharField(max_length=512, required=False, empty_value="", widget=forms.Textarea(attrs={
        "class":"form-control",
        "rows":"3",
        "placeholder":"Description of the listing (optional)"
    }))

    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0, required=True, widget=forms.NumberInput(attrs={
        "class":"form-control",
        "placeholder":"Starting bid"
    }))

    image_url = forms.URLField(max_length=256, required=True, widget=forms.URLInput(attrs={
        "class":"form-control",
        "placeholder":"Image URL"
    }))

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        empty_label="Select a category (optional)",
        required=False,
        initial="", 
        widget=forms.Select(attrs={"class":"form-control"}))
    
class PlaceBidForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={
        "class":"form-control",
        "placeholder":"Bid"
    }))