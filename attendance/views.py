from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Attendance
from .forms import DateRangeForm
from employee.models import EmployeeUser
from django.db.models import Sum, F, ExpressionWrapper, DurationField
from datetime import timedelta
from .decorators import admin_required, manager_required
from datetime import date, timedelta

def home(request):
    return redirect('attendance:register_attendance')

def register_attendance(request):
    user = request.user
    records = Attendance.objects.filter(employeeuser__id=user.id).order_by('-time_in')[:10]
    today = timezone.now()
    return render(request, 'attendance/employee_register_attendance.html', {'records': records, 'user':user, 'today':today})


def time_in(request):
    employee_user = get_object_or_404(EmployeeUser, pk=request.user.id)
    now = timezone.now()
    Attendance.objects.create(employeeuser=employee_user, time_in=now)
    return redirect('attendance:register_attendance')


def time_out(request):
    user = request.user
    now = timezone.now()
    try:
        last_record = Attendance.objects.filter(employeeuser=user, time_out__isnull=True).latest('time_in')
        last_record.time_out = now
        last_record.save()
    except Attendance.DoesNotExist:
        pass  # Optionally handle no time-in before time-out
    return redirect('attendance:register_attendance')


# Attendance summary per employee; unused
"""@admin_required
def attendance_summary(request):
    summary = None
    days = request.GET.get('days')

    if days:
        try:
            days = int(days)
            start_date = timezone.now() - timedelta(days=days)
            end_date = timezone.now()

            # Total time per user
            attendance = Attendance.objects.filter(time_in__gte=start_date, time_out__isnull=False)
            attendance = attendance.annotate(
                duration=ExpressionWrapper(F('time_out') - F('time_in'), output_field=DurationField())
            ).values('employeeuser__username').annotate(total=Sum('duration'))

            summary = attendance
        except ValueError:
            days = None

    return render(request, 'attendance/attendance_summary.html', {'summary': summary})
"""
@manager_required
def attendance_record(request):
    form = DateRangeForm(request.POST or None)
    start = end = num_days = 0
    if request.method == "POST" and form.is_valid():
        start = form.cleaned_data['start_date']
        end = form.cleaned_data['end_date']
    else:
        num_days = 15
    recs = {}
    today = date.today()
    days_ago = today - timedelta(days=num_days)
    employees = EmployeeUser.objects.filter(is_active=True)
    attendance_records = Attendance.objects.all()
    for employee in employees:
        if start and end: 
            records = attendance_records.filter(employeeuser=employee, time_in__lte=end, time_in__gte=start).order_by('-pk')
        else:
            records = attendance_records.filter(employeeuser=employee, time_in__gte=days_ago).order_by('-pk')
        data = []
        total_duration = timedelta()
        hours = 0
        if records:
            for rec in records:
                if rec.time_out and rec.time_in:
                    duration = rec.time_out - rec.time_in
                else:
                    duration = timedelta()
                str_duration = str(duration).split(".")[0]
                data.append({'time_in':rec.time_in, 'time_out':rec.time_out, 'duration': str_duration})
                total_duration += duration
            hours = total_duration.total_seconds() / 3600
            data.append({'hours': round(hours, 2)})
            recs.update({ employee:data})
    return render(request, 'attendance/attendance_record.html', {'records':recs, 'form':form})

    
