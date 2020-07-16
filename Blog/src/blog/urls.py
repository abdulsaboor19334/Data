from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from new.views import homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('new.urls', namespace='blog')),
    path('', homeview, name= 'home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)