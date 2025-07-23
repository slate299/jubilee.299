from django import forms
from .models import Concern

class ConcernForm(forms.ModelForm):
    ISSUES_CHOICES = [
        ('Economy', 'Economy'),
        ('Corruption', 'Corruption'),
        ('Unemployment', 'Unemployment'),
        ('Healthcare', 'Access to affordable healthcare'),
        ('Water', 'Water'),
        ('Education', 'Education'),
        ('Infrastructure', 'Infrastructure'),
        ('Housing', 'Housing'),
        ('Climate Change', 'Climate Change'),
    ]

    issues = forms.MultipleChoiceField(
        choices=ISSUES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Concern
        fields = [
            'first_name',
            'second_name',
            'surname',
            'phone_number',
            'email',
            'issues',
            'other_issues',
            'story',
            'thanks',
        ]
