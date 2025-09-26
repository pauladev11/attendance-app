import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import EmployeeUser #, Payroll, PayrollEmployee, EmployeeCashAdvance
from .forms import EmployeeUserForm #PayrollForm, payrollemployeeformset

from django.http import HttpResponse
from django.db.models import Sum
#from django.template.loader import render_to_string
#from weasyprint.fonts import FontConfiguration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from weasyprint import HTML
from django.contrib.auth.decorators import login_not_required

def list_employee(request):
    employees = EmployeeUser.objects.filter(is_active=True).order_by('lastname')
    args = {'employees': employees }
    return render(request, 'employee/list_employee.html', args)

def edit_employee(request, pk):
    context = {}
    employee = get_object_or_404(EmployeeUser, pk=pk)
    if request.method == 'GET':
        form = EmployeeUserForm(instance=employee)
    else:
        form = EmployeeUserForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            return redirect('employee:list_employee')
    context = {'form': form, 'employee':employee}
    return render(request, 'employee/edit_employee.html', context)

def create_employee(request):
    context = {}
    if request.method == 'POST':
        form = EmployeeUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            name = instance.firstname + ' ' + instance.lastname
            context.update({'message': name + ' saved.'})
    else:
        form = EmployeeUserForm()
    context.update({'form':form})
    return render(request, 'employee/edit_employee.html', context)

@login_not_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('attendance:register_attendance')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('employee:login')

"""def payroll(request):
    context = {'title':'Payroll'}
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            sched = form.cleaned_data.get('payroll_sched')
            request.session['payroll_sched'] = sched
            employees = Employee.objects.filter(payroll_sched=sched,
                                        active=True).order_by('lastname')
            data = []
            for e in employees:
                data.append({'employee':e})
            payrollemployeeform = payrollemployeeformset(initial=data)
            context.update({'payrollemployeeform': payrollemployeeform})
            context.update({'payroll_sched': sched})
    else:
        form = PayrollForm()
    context.update({'form': form})
    return render(request, 'employee/payroll.html', context) 

def create_payroll(request):
    context = {'title':'Payroll Created'}
    if request.method == 'POST':
        payrollemployeeform = payrollemployeeformset(request.POST)
        if payrollemployeeform.is_valid():
            sched = request.session.get('payroll_sched')
            payroll = Payroll(date=datetime.date.today(),
                                        payroll_sched=sched)
            payroll.save()
            for pe_form in payrollemployeeform:
                i = pe_form.save(commit=False)
                i.payroll = payroll
                i.save()
            del request.session['payroll_sched']
        payrollemployees = PayrollEmployee.objects.filter(payroll=payroll)
        context.update({'employees':payrollemployees})
        context.update({'payroll': payroll})

    return redirect('employee:list_payroll')

def list_payroll(request):
    context = {'title' : 'Payroll List'}
    payroll = Payroll.objects.all().order_by('-date')
    context.update({'payroll': payroll})
    return render(request, 'employee/list_payroll.html', context)

def list_payroll_employees(request, pk):
    payroll = Payroll.objects.get(id=pk)
    d = payroll.date
    payroll_date = d.strftime("%m/%d/%Y")
    payroll_sched = payroll.get_payroll_sched_display()
    title = 'Employees in Payroll Date: ' + payroll_date + ' (' + payroll_sched + ')'
    context = {'title' : title }
    employees = PayrollEmployee.objects.filter(payroll=payroll)
    total = 0
    for e in employees:
        e.total_days = (6 - e.absent) + e.overtime
        e.gross = round(e.employee.rate * e.total_days)
        e.net = e.gross - e.deduction
        total += e.net
    context.update({'payroll': payroll})
    context.update({'total':total})
    context.update({'payroll_employees': employees})
    return render(request, 'employee/list_payroll_employees.html', context)

def print_payroll_employee(request, payroll_pk):
    payroll = get_object_or_404(Payroll, pk=payroll_pk)
    payroll_employees = PayrollEmployee.objects.select_related('employee'
                                        ).filter(payroll=payroll).order_by('employee__lastname')
    for e in payroll_employees:
        e.total_days = (6 - e.absent) + e.overtime
        e.gross = round(e.employee.rate * e.total_days)
        e.net = e.gross - e.deduction
    context = {'employees' : payroll_employees}
    context.update({'payroll': payroll})
    
    html_string = render_to_string('employee/print_payroll_employee.html', context)
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=print_payroll.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    font_config = FontConfiguration()
    HTML(string=html_string).write_pdf(response, font_config=font_config)
    return response
"""
