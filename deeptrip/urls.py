import smart_selects
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from tours import urls
from tours.views import ToursApiView

router = SimpleRouter()
router.register('api/tours', ToursApiView)

urlpatterns = []

urlpatterns += router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('', include('base.urls')),
    path('', include('tours.urls_api')),
    path('magazine/', include('articles.urls')),
    path('<slug:city_slug>/', include('tours.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

