from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'khodro'

urlpatterns = []

router = SimpleRouter()

router.register("", views.KhodroViewSet)

urlpatterns += router.urls