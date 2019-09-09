from django import forms
from django.forms import ModelForm
from emplpoyeeDBapp.models import *

class DepartmentForm(forms.Form):
    DepartmentCode = forms.CharField(label="Department Code",required=True)
    DepartmentName = forms.CharField(label="Department Name",required=True)

    class Meta:
        model = Department
        fields = ['DepartmentCode','DepartmentName']

class DesignationForm(forms.Form):
    DesignationCode = forms.CharField(label="Designation Code", required=True)
    DesignationName = forms.CharField(label="Designation Name",required=True)

    class Meta:
        model = Designation
        fields = ['DesignatioCode','DesignatioName']
