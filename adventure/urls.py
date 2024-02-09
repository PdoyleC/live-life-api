from django.urls import path
from adventure import views

urlpatterns = [
    path('adventure/', views.AdventureList.as_view()),
    path('adventure/<int:pk>/', views.AdventureDetail.as_view())
]
