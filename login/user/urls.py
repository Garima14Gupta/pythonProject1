from django.urls import path
from .views import Userviewset

urlpatterns = [
    path('login/',Userviewset.as_view({'post':'create'},name='userviewset'))
]