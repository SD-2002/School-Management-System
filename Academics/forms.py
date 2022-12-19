from django import forms
from . models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
            'Roll_No': forms.TextInput(attrs={'class': 'form-control'}),
            'Attendance_class': forms.TextInput(attrs={'class': 'form-control'}),
        }