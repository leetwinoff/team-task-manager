from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from tasks.models import Task, Worker, Position


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline_date",
            "priority",
            "task_type",
            "is_completed",
            "assignees",
        ]
        widgets = {"deadline_date": forms.TextInput(attrs={"type": "datetime-local"})}


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ["name"]


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(years_of_experience):
    if years_of_experience < 0:
        raise ValidationError("Years of experience should be positive")
    elif years_of_experience == 0:
        raise ValidationError(
            "Years of experience should be more than 1 Year for this position"
        )
    elif years_of_experience >= 50:
        raise ValidationError(
            "If you have worked for more than 50 years, please enter '50' as the maximum allowable value."
        )
    return years_of_experience


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by position"}),
    )


class WorkerSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by last name"}),
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by task name"}),
    )
