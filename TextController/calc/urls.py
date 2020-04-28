from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("newpage",views.newpage,name="newpage"),
     
    
       path("analyze",views.analyze,name="analyze")
        

]