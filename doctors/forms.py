from django import forms
from doctors.models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'



class DoctorSearchForm(forms.Form):
    search_query = forms.CharField(required=False)
