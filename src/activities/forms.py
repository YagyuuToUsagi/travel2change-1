from django import forms

from .models import Activity, LatestActivityPlugin


class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'region', ]


class HighlightsForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['highlights', ]


class RequirementsForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['requirements', ]


class TagsForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['tags', ]


class PriceForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['price', ]


class LocationForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['address', 'latitude', 'longitude', ]
        widgets = {
            'latitude': forms.HiddenInput(attrs={
                'id': 'lat_field'
            }),
            'longitude': forms.HiddenInput(attrs={
                'id': 'lng_field'
            })
        }


""" Form that corresponds to each step of the activity creation """
ACTIVITY_CREATE_FORMS_LIST = [
    ("0", BasicInfoForm),
    ("1", HighlightsForm),
    ("2", RequirementsForm),
    ("3", TagsForm),
    ("4", PriceForm),
    ("5", LocationForm),
]

""" CMS Wizard Form """
class ActivityWizardForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = [
            'slug', 'review_count', 'created', 'modified',
        ]


class ActivityUpdateForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = (
            'title',
            'region',
            'description',
            'highlights',
            'requirements',
            'tags',
            'price',
            'address',
            'latitude',
            'longitude',
        )
        widgets = {
            'latitude': forms.TextInput(attrs={
                'id': 'lat_field',
            }),
            'longitude': forms.TextInput(attrs={
                'id': 'lng_field',
            })
        }


"""
============== ACTIVITY PLUGIN FORMS =================
"""

class LatestActivitiesPluginForm(forms.ModelForm):
    class Meta:
        model = LatestActivityPlugin
        fields = ['latest_activities']
