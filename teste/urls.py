from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from teste import views

urlpatterns = [
    path('teste/', views.teste),
]

urlpatterns = format_suffix_patterns(urlpatterns)