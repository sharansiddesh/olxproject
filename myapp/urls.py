from django.urls import path
from myapp import views
app_name='myapp'

urlpatterns = [
    path('home/',views.home,name="home"),
    path('motorcycle/',views.motorcycle,name="motorcycle"),
    path('house/',views.house,name="house"),
    path('scooters/',views.scooters,name="scooters"),
    path('commercial/',views.commercial,name="commercial"),
    path('mobilephone/',views.mobilephone,name="mobilephone"),
]

