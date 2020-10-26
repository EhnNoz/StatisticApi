from testapp import views
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('session', views.SessionViewSets, basename='sessions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
