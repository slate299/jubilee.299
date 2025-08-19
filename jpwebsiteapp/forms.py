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
        required=False,  # Makes the checkbox field optional
        help_text="Select all that apply (optional)"
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
        widgets = {
            'story': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Optional - tell us more about your concerns...'}),
            'thanks': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Optional - share positive feedback if you wish...'}),
        }
        labels = {
            'second_name': 'Middle Name (Optional)',
            'email': 'Email (Optional)',
            'other_issues': 'Other Issues (If not listed above)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mark required fields with an asterisk
        for field_name, field in self.fields.items():
            if field.required:
                field.label = f"{field.label} *"
            if not field.required and field_name != 'issues':
                field.widget.attrs['placeholder'] = 'Optional'