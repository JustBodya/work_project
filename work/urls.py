from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('employee/', EmployeeAPIList.as_view()),
    path('employee/<int:pk>/', EmployeeAPIDetail.as_view()),
    path('profitability/', ProfitabilityAPIList.as_view(), name='profitability-list'),
    path('profitability/<int:pk>/', ProfitabilityAPIDetail.as_view()),
    path('employee/<int:pk>/profitability/', EmployeeProfitabilityAPIView.as_view()),
    path('export/', export_to_excel, name='export-to-excel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)