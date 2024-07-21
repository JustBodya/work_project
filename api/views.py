from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Employee, Profitability
from .serializers import EmployeeSerializer, ProfitabilitySerializer
from .permissions import IsAdminorReadOnly


class EmployeeAPIList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class EmployeeAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated, )


class EmployeeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminorReadOnly, )


class ProfitabilityAPIList(generics.ListCreateAPIView):
    queryset = Profitability.objects.all()
    serializer_class = ProfitabilitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ProfitabilityAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profitability.objects.all()
    serializer_class = ProfitabilitySerializer
    permission_classes = (IsAuthenticated, )


class ProfitabilityAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Profitability.objects.all()
    serializer_class = ProfitabilitySerializer
    permission_classes = (IsAdminorReadOnly, )
