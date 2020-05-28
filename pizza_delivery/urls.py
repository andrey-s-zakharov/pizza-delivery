from django.contrib import admin
from django.urls import path, include

from pizzas import urls as api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api, namespace='api')),
]
