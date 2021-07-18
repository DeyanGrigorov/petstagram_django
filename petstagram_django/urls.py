from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from petstagram_django import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('petstagram_django.common.urls')),
                  path('pets/', include('petstagram_django.pets.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
