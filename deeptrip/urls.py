from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tours import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('<str:city_slug>/', include('tours.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
