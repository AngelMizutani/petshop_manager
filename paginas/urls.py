from django.urls import path
from .views import Index

urlpatterns = [
    # path('inicio/', Index.as_view(), name='index'),
    path('', Index.as_view(), name='index'),
]