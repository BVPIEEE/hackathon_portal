from django import forms
from complexModules.models import scoringModel


class scoringForm(forms.ModelForm):
    class Meta:
        model = scoringModel
        fields = "__all__"
