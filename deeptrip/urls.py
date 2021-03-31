import smart_selects
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('', include('base.urls')),
    path('', include('tours.urls.api')),
    path('_nested_admin/', include('nested_admin.urls')),
    path('magazine/', include('articles.urls')),
    path('<slug:city_slug>/', include('tours.urls.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

