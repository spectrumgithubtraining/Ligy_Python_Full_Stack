from django.urls import path
from.import views


urlpatterns = [
    path("",views.index,name='index'),
    path('reg/',views.reg,name="reg"),
    path('forgot/',views.forgot,name="fogot"),
 
]