from django.contrib import admin
from .models import EmployeeUser #, Payroll, PayrollEmployee, EmployeeCashAdvance
from django.contrib.auth.admin import UserAdmin

#admin.site.register(Payroll)
#admin.site.register(PayrollEmployee)

#def set_fully_paid_t(self, request, queryset):
#        for i in queryset:
#            i.fully_paid = True
#            i.save()

#set_fully_paid_t.short_description = 'Set Fully Paid to True'

#class EmployeeCashAdvanceAdmin(admin.ModelAdmin):
#    list_display = ('fully_paid', 'total', 'date', 'amortization', 'employee')
#    list_filter = ['fully_paid']
#    actions = [set_fully_paid_t, ]

class EmployeeUserAdmin(UserAdmin):
    list_display = ('username', 'firstname', 'lastname', 'manager', 'is_active','birth_date')


    
#admin.site.register(EmployeeCashAdvance)
# EmployeeCashAdvanceAdmin)
admin.site.register(EmployeeUser, EmployeeUserAdmin)
