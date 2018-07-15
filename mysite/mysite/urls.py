from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('personal.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^shop/', include('shop.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)