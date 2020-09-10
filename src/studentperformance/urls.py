from django.urls import path

from .views import PerformanceTestView, PerformanceDetailView

urlpatterns = [
    path('test/', PerformanceTestView.as_view(), name='performance_test'),
    path('<int:pk>/', PerformanceDetailView.as_view(), name="performance_detail")
]
