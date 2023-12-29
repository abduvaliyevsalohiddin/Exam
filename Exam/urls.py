from django.contrib import admin
from django.urls import path
from asosiy.views import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Imtihoz uchun yozilgan API",
        default_version="V1",
        description="Test",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True,
)

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

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

]
