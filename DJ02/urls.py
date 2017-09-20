from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^giving/', include('giving.urls', namespace="giving")),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('giving.urls', namespace="giving")),
]
