from rest_framework import serializers
from .models import Employee, Profitability

class ProfitabilitySerializer(serializers.ModelSerializer):
    employee_full_name = serializers.ReadOnlyField(source='employee.full_name')
    
    class Meta:
        model = Profitability
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def get_profitability(self, obj):
            profitabilities = Profitability.objects.filter(employee=obj)
            return ProfitabilitySerializer(profitabilities, many=True).data
