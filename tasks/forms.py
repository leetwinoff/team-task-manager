from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from tasks.models import Task, Worker


class TaskForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
            "years_of_experience"
        )

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(years_of_experience):
    if years_of_experience < 0:
        raise ValidationError("Years of experience should be positive")
    elif years_of_experience == 0:
        raise ValidationError("Years of experience should be more than 1 Year for this position")
    return years_of_experience
