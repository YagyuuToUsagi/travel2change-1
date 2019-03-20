from django import forms
import django_filters
from .models import Activity, Region, Tag

class ActivityFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    region = django_filters.ModelChoiceFilter(queryset=Region.objects.all())
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Activity
        fields = ['title', 'region', 'tags', ]
