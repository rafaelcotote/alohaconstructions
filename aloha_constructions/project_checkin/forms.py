from django import forms
from .models import CheckinRegister
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from tempus_dominus.widgets import DateTimePicker

class CheckinRegisterForm(forms.ModelForm):
    TYPE_CHOICES = [
        (CheckinRegister.CHECKIN, 'Check-in'),
        (CheckinRegister.CHECKOUT, 'Check-out'),
    ]

    type_register = forms.ChoiceField(choices=TYPE_CHOICES, initial=CheckinRegister.CHECKIN)

    class Meta:
        model = CheckinRegister
        fields = ['employee', 'project', 'date_register', 'activity', 'type_register']
        widgets = {
            'date_register': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "sideBySide": True}),
            'type_register': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        if user:
            self.fields['employee'].initial = user.username
        else:
            self.fields['employee'].widget.attrs['readonly'] = True

        
        self.fields['activity'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a description'})
