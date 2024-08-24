
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #path('',ngosite.)
    path('admin/', admin.site.urls),
    path('',include('ngosite.urls'))
]
