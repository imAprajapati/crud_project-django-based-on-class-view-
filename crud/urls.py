from django.urls import path
from .views import *

urlpatterns = [
    path('',Add_Show.as_view(),name='addshow'),
    path('delete/<int:id>',Delete_Data.as_view(),name='deletedata'),
    path('<int:id>/',Update_Data.as_view(),name="updatedata"),
]
