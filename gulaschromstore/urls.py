from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from gulaschromstore.settings import MEDIA_URL, MEDIA_ROOT

from roms.views import RomList


urlpatterns = [
    url(r'^$', RomList.as_view()),
    url(r'^roms/', include('roms.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
