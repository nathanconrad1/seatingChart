from django.urls import path
from .views import indexPageView, seatingChartView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('chart', seatingChartView, name='chart'),
]
