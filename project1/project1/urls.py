
from django.contrib import admin
from django.urls import path,include
from project1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path("",include('blog.urls')),
    path('blog/',views.Blog)
]
