from django.urls import path

from collector.views import index
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index.index),
]
