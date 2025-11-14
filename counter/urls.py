from django.urls import path
from .views import increment_download

urlpatterns = [
    path('increment/', increment_download, name='increment_download'),
]
