from django.urls import path
from .views import success, fail

urlpatterns = [

    path('success/<str:message>', success, name='success'),
    path('fail/<str:message>', fail, name='fail'),


]
