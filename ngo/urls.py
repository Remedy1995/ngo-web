from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include


urlpatterns = [
    #path('',ngosite.)
    path('admin/', admin.site.urls),
    path('',include('ngosite.urls')),
    path('volunteers/', include('volunteers.urls')),  # Include volunteer app URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)