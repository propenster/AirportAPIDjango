from django.urls import path
from .views import AirportListView, AirportDetailView

urlpatterns = [
    path('airports', AirportListView.as_view(), name='all_airports'),
    path('airports/<int:id>', AirportDetailView.as_view(), name='single_airport'),
    
]
