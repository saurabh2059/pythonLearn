
from django.contrib import admin
from django.urls import path,include
from project1 import views
from django.conf.urls.static import static

from project1 import settings
# from blog import blogs


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.Home),
    path('',views.BlogPage),
    path("",include('blog.urls')),
    path('blog/',views.Blog)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT)