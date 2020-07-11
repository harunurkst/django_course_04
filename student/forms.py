from django import forms
from .models import StudentList


class StudentCreateForm(forms.ModelForm):
    # roll = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # std_class = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = StudentList
        exclude = ('gpa',)

        GENDER_CHOICE = (
            ('male', 'Male'),
            ('female', 'Female'),
        )
        widgets = {
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'std_class': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=GENDER_CHOICE, attrs={'class': 'form-control'}),
        }


class ResultForm(forms.Form):
    std_class = forms.CharField()
    roll = forms.IntegerField()