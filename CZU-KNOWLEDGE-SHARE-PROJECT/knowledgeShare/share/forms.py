from django import forms
from django.forms import fields

from .models import Faculty, StudyType, Subject, File


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["subject_code", "name"]
        widgets = {
            "subject_code": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        subject_code = cleaned_data.get("subject_code")

        if Subject.objects.filter(subject_code=subject_code).exists():
            self.add_error("subject_code", "Subject code already exist")


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = [
            "name",
        ]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class StudyTypeForm(forms.ModelForm):
    class Meta:
        model = StudyType
        fields = [
            "name",
        ]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = [
            "subject",
            "title",
            "cover_image",
            "file_link",
            "description",
            "is_public",
        ]
        widgets = {
            "subject": forms.Select(attrs={"class": "form-control mb-2"}),
            "title": forms.TextInput(attrs={"class": "form-control mb-2"}),
            "cover_image": forms.FileInput(attrs={"class": "form-control mb-2"}),
            "file_link": forms.FileInput(attrs={"class": "form-control mb-2"}),
            "description": forms.Textarea(attrs={"class": "form-control mb-2"}),
        }
        labels = {"subject": "SUBJECT"}
