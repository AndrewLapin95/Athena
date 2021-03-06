from django import forms

from .models import Employee, EmergencyContact, Department, Designation, Vacation

class EmployeeUpdateForm(forms.ModelForm):
    """
    Form to update employee's personal information
    """
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'birthday',
            'gender',
            'address',
        ]

class EmergencyContactCreateForm(forms.ModelForm):
    """
    Form to create a new emergency contact for a given user
    """
    class Meta:
        model = EmergencyContact
        fields = [
            'name',
            'relationship',
            'birthday',
            'phone_number',
        ]

class VacationCreateForm(forms.ModelForm):
    """
    Form to create a new emergency contact for a given user
    """
    class Meta:
        model = Vacation
        fields = [
            'start_date',
            'end_date',
        ]

class VacationUpdateForm(forms.ModelForm):
    """
    Form to update vacation request for a given user
    """
    class Meta:
        model = Vacation
        fields = [
            'status',
        ]
