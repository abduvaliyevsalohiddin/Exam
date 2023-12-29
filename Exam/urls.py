from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suvlar/', SuvlarAPi.as_view()),
    path('suv/<int:pk>/', SuvAPi.as_view()),

    path('mijozlar/', MijozlarAPi.as_view()),
    path('buyurtmalar/', BuyurtmalarAPi.as_view()),
    path('adminlar/', AdminlarAPi.as_view()),
    path('haydovchilar/', HaydovchilarAPi.as_view()),
    path('mijoz/<int:pk>/', MijozAPi.as_view()),
    path('admin/<int:pk>/', AdminAPi.as_view()),
    path('haydovchi/<int:pk>/', HaydovchiAPi.as_view()),

]
