from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', EmployeeAPIList.as_view()),
    path('employee/<int:pk>/', EmployeeAPIUpdate.as_view()),
    path('employeedelete/<int:pk>/', EmployeeAPIDestroy.as_view()),
    path('profitability/', ProfitabilityAPIList.as_view()),
    path('profitability/<int:pk>/', ProfitabilityAPIUpdate.as_view()),
    path('profitabilitydelete/<int:pk>/', ProfitabilityAPIDestroy.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

