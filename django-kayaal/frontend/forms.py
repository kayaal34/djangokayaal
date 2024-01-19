from django import forms


class AddForm(forms.Form):
    day = forms.IntegerField(max_value=30, min_value=1, label="День")