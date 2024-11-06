# myapp/forms.py

from django import forms

class JoinTeamForm(forms.Form):
    code = forms.CharField(max_length=10, label='Team Code')
