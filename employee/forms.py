import datetime
from django import forms
from .models import EmployeeUser #, PayrollEmployee, Payroll
from django.forms import formset_factory

class EmployeeUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(EmployeeUserForm, self).__init__(*args, **kwargs)
       fields = [
                'username'
                'firstname',
                'lastname',
                'password', 
                'birth_date',
                'is_active'
                'manager']

    class Meta:
        model = EmployeeUser
        fields = [
                'username',
                'password',
                'firstname',
                'lastname', 
                'birth_date',
                'is_active',
                'manager']
        widgets = {
                'password': forms.PasswordInput(),
                'manager': forms.CheckboxInput(),
            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_superuser = False
        if commit:
            user.save()
        return user

"""
class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        exclude = []

    payroll_sched = forms.ChoiceField(choices=Employee.payroll_sched_choices)
    date = forms.DateField(initial=datetime.date.today(),
                          widget=forms.widgets.DateInput(format="%m/%d/%Y"))

   
    def clean(self):
        data = super().clean()
        schedule = data.get('payroll_sched')
        date = data.get('date')
        if schedule == 'w':
            if date.strftime('%w') != '6':
                raise forms.ValidationError("Weekly Payroll is only on Saturday!")
        elif schedule == 'm':
            if date.strftime('%d') not in [15, 30, 31]:
                raise forms.ValidationError("Monthly Payroll is only on the 15th and 30th/31st!")
        elif schedule == 'c':
            if date.strftime('%w') != '6':
                raise forms.ValidationError("Construction Payroll is only on Saturday!")
        return data
        

class PayrollEmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PayrollEmployeeForm, self).__init__(*args, **kwargs)
        fields = [
              'employee',
              'absent', 
              'deduction',
              ]

    class Meta:
        model = PayrollEmployee
        exclude = ['payroll']

payrollemployeeformset = formset_factory(PayrollEmployeeForm, extra=0)
"""
