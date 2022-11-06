from django.urls import path
from .views import indexA, indexB, indexC

urlpatterns = [
    path('a/', indexA),
    path('b/', indexB),
    path('c/', indexC)
]