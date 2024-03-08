from django.urls import path
from .views import TripList, TripDetail

urlpatterns = [
    path('trips/', TripList.as_view()),
    path('trips/<int:pk>/', TripDetail.as_view()),
]
