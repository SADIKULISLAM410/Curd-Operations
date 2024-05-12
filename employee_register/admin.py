from django.contrib import admin
from employee_register.models import Position , Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'emp_code', 'mobile', 'position')
    
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
