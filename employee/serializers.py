from rest_framework import serializers
from employee.models import Employees



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Address',
                  'Phone',
                  'Email',
                  'PhotoFileName'

                  )