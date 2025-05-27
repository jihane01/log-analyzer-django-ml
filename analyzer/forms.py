# analyzer/forms.py
from django import forms

class LogForm(forms.Form):
    log_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
