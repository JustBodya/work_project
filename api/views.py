import openpyxl
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.decorators import user_passes_test
from .models import Employee, Profitability
from .serializers import EmployeeSerializer, ProfitabilitySerializer
from .permissions import IsAdminOrReadOnly


def index(request):
    return render(request, 'index.html')


class EmployeeAPIList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]


class EmployeeAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProfitabilityAPIList(generics.ListCreateAPIView):
    queryset = Profitability.objects.all()
    serializer_class = ProfitabilitySerializer
    permission_classes = [IsAdminOrReadOnly]


class ProfitabilityAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profitability.objects.all()
    serializer_class = ProfitabilitySerializer
    permission_classes = [IsAdminOrReadOnly]


class EmployeeProfitabilityAPIView(generics.ListAPIView):
    serializer_class = ProfitabilitySerializer

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return Profitability.objects.filter(employee_id=employee_id)


@user_passes_test(lambda u: u.is_staff, login_url='/accounts/login/')
def export_to_excel(request):

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Employees and Profitability"


    headers = [
        'ID', 'Full Name', 'Passport Data', 'Hours Worked', 'Total Hours Worked',
        'Deductions', 'Total Earnings', 'Profitability Client Payment',
        'Employee Salary', 'Accommodation Payment', 'Food Payment',
        'Transport Payment', 'Agency Payment', 'Total Profitability',
        'Additional Expenses', 'Fines'
    ]
    ws.append(headers)


    employees = Employee.objects.all()
    for employee in employees:
        profitabilities = Profitability.objects.filter(employee=employee)
        for profitability in profitabilities:
            row = [
                employee.id, employee.full_name, employee.passport_data,
                employee.hours_worked, employee.total_hours_worked,
                employee.deductions, employee.total_earnings,
                profitability.client_payment, profitability.employee_salary,
                profitability.accommodation_payment, profitability.food_payment,
                profitability.transport_payment, profitability.agency_payment,
                profitability.total_profitability, profitability.additional_expenses,
                profitability.fines
            ]
            ws.append(row)

    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=employees_profitability.xlsx'
    wb.save(response)
    return response