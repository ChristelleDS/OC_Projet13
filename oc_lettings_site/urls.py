from django.contrib import admin
from django.urls import path, include


app_name = 'oc_lettings_site'

urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
