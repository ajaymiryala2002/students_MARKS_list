from django import forms
from marks_list.models import student
class studentFORM(forms.ModelForm):
    class Meta:
        model=student
        fields= '__all__'